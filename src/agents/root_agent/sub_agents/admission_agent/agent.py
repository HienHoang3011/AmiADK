from google.adk.agents import Agent
from . import prompt, tools

MODEL = "gemini-2.0-flash"
admission_agent = Agent(
    name="admission_agent",
    model=MODEL,
    description="Cung cấp thông tin chi tiết và hướng dẫn về quy trình tuyển sinh",
    instruction=prompt.ADMISSION_AGENT_PROMPT
)