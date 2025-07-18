import logging
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv

from livekit import api
from livekit.agents import (
    Agent,
    AgentSession,
    ChatContext,
    JobContext,
    JobProcess,
    RoomInputOptions,
    RoomOutputOptions,
    RunContext,
    WorkerOptions,
    cli,
    metrics,
)
from livekit.agents.job import get_job_context
from livekit.agents.llm import function_tool
from livekit.agents.voice import MetricsCollectedEvent

# Use built-in plugins from livekit.agents
from livekit.agents.stt import WhisperSTT
from livekit.agents.tts import SileroTTS
from livekit.agents.vad import SileroVAD
from livekit.agents.llm import OllamaLLM

logger = logging.getLogger("multi-agent")

load_dotenv()

common_instructions = (
    "Your name is Echo. You are a story teller that interacts with the user via voice. "
    "You are curious and friendly, with a sense of humor."
)

@dataclass
class StoryData:
    name: Optional[str] = None
    location: Optional[str] = None

class IntroAgent(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=(
                f"{common_instructions} Your goal is to gather a few pieces of "
                "information from the user to make the story personalized and engaging. "
                "You should ask the user for their name and where they are from. "
                "Start the conversation with a short introduction."
            )
        )

    async def on_enter(self):
        self.session.generate_reply()

    @function_tool
    async def information_gathered(
        self,
        context: RunContext[StoryData],
        name: str,
        location: str,
    ):
        context.userdata.name = name
        context.userdata.location = location

        story_agent = StoryAgent(name, location)

        logger.info(
            "Switching to the story agent with the provided user data: %s", context.userdata
        )
        return story_agent, "Let's start the story!"

class StoryAgent(Agent):
    def __init__(self, name: str, location: str, *, chat_ctx: Optional[ChatContext] = None) -> None:
        super().__init__(
            instructions=(
                f"{common_instructions} You should use the user's information in "
                "order to make the story personalized. "
                "Create the entire story, weaving in elements of their information, and make it "
                "interactive, occasionally interacting with the user. "
                "Do not end on a statement where the user is not expected to respond. "
                "When interrupted, ask if the user would like to continue or end. "
                f"The user's name is {name}, from {location}."
            ),
            llm=OllamaLLM(model="gemma:2b"),  # Updated
            tts=SileroTTS(voice="en_0"),      # Updated
            chat_ctx=chat_ctx,
        )

    async def on_enter(self):
        self.session.generate_reply()

    @function_tool
    async def story_finished(self, context: RunContext[StoryData]):
        self.session.interrupt()

        await self.session.generate_reply(
            instructions=f"Say goodbye to {context.userdata.name}", allow_interruptions=False
        )

        job_ctx = get_job_context()
        await job_ctx.api.room.delete_room(api.DeleteRoomRequest(room=job_ctx.room.name))

def prewarm(proc: JobProcess):
    proc.userdata["vad"] = SileroVAD.load()  # Updated

async def entrypoint(ctx: JobContext):
    await ctx.connect()

    session = AgentSession[StoryData](
        vad=ctx.proc.userdata["vad"],
        llm=OllamaLLM(model="gemma:2b"),  # Updated
        stt=WhisperSTT(model="base"),      # Updated
        tts=SileroTTS(voice="en_0"),       # Updated
        userdata=StoryData(),
    )

    usage_collector = metrics.UsageCollector()

    @session.on("metrics_collected")
    def _on_metrics_collected(ev: MetricsCollectedEvent):
        metrics.log_metrics(ev.metrics)
        usage_collector.collect(ev.metrics)

    async def log_usage():
        summary = usage_collector.get_summary()
        logger.info(f"Usage: {summary}")

    ctx.add_shutdown_callback(log_usage)

    await session.start(
        agent=IntroAgent(),
        room=ctx.room,
        room_input_options=RoomInputOptions(),
        room_output_options=RoomOutputOptions(transcription_enabled=True),
    )

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))