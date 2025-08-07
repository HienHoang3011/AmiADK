from google.adk.agents import Agent
from . import prompt, tools
MODEL = "gemini-2.0-flash"
general_agent = Agent(
    name="general_agent",
    model=MODEL,
    description="General agent",
    instruction=prompt.GENERAL_AGENT_PROMPT,
    tools= []
)
