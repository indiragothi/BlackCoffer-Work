import asyncio
from livekit import agents, rtc
from livekit.agents import JobContext, WorkerOptions, cli
from livekit.agents.llm import ChatContext, ChatMessage
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import deepgram, silero
import pyttsx3
from transformers import pipeline

# Load offline HuggingFace LLM
chatbot = pipeline("text-generation", model="microsoft/phi-1_5", max_new_tokens=100)

# Init pyttsx3
tts_engine = pyttsx3.init()

# Function to get local AI response (free)
async def get_local_response(prompt: str) -> str:
    result = chatbot(prompt)
    return result[0]["generated_text"].replace(prompt, "").strip()

# Function: say text using pyttsx3 (offline TTS)
async def say_text(text: str):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, tts_engine.say, text)
    await loop.run_in_executor(None, tts_engine.runAndWait)

async def entrypoint(ctx: JobContext):
    await ctx.connect()
    print(f"Connected to room: {ctx.room.name}")

    chat_ctx = ChatContext(messages=[
        ChatMessage(role="system", content="You are an offline voice assistant. Speak clearly and keep answers short.")
    ])

    assistant = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=deepgram.STT(),  # Deepgram for Speech-to-Text
        llm=None,            # We'll bypass this and use local HuggingFace
        tts=None,            # We'll use pyttsx3 directly
        chat_ctx=chat_ctx,
    )

    async def on_user_speech(text: str):
        print(f"User said: {text}")
        chat_ctx.messages.append(ChatMessage(role="user", content=text))

        response = await get_local_response(text)
        print(f"Bot says: {response}")

        chat_ctx.messages.append(ChatMessage(role="assistant", content=response))
        await say_text(response)

    assistant.on("transcription", lambda txt: asyncio.create_task(on_user_speech(txt)))
    assistant.start(ctx.room)

    await asyncio.sleep(1)
    await say_text("Hello! I'm ready to help you.")

    while ctx.room.connection_state == rtc.ConnectionState.CONN_CONNECTED:
        await asyncio.sleep(1)

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
