import logging
from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    RunContext,
    WorkerOptions,
    cli,
    function_tool,
)
from livekit.plugins import groq, silero

# Load environment variables
load_dotenv(dotenv_path=".env")

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

# Tool to look up weather
@function_tool
async def lookup_weather(
    context: RunContext,
    location: str,
):
    """Used to look up weather information."""
    return {"weather": "sunny", "temperature": 70}

# Main entrypoint
async def entrypoint(ctx: JobContext):
    await ctx.connect()

    agent = Agent(
        instructions="""
            You are a helpful and friendly voice assistant built by LiveKit.
            Greet the user, and respond to their requests.
            Only use the `lookup_weather` tool if the user specifically asks for weather information.
            """,
        tools=[lookup_weather],
    )

    session = AgentSession(
        vad=silero.VAD.load(),  # Make sure this detects voice correctly
        stt=groq.STT(),          
        llm=groq.LLM(model="llama-3.3-70b-versatile"),
        tts=groq.TTS(model="playai-tts"),
    )

    await session.start(agent=agent, room=ctx.room)

    # Initial prompt
    await session.generate_reply(instructions="Say hello, then ask the user how their day is going and how you can help.")

    # Important: Start listening/responding to user input
    await session.run(agent=agent)

# Run app
if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
