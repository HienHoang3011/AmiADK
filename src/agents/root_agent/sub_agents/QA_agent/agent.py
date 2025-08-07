from google.adk.agents import Agent
from . import prompt, tools

MODEL = "gemini-2.0-flash"
qa_agent = Agent(
    name="QA_agent",
    model=MODEL,
    description="Trợ lý ảo hỗ trợ người dùng trong việc tìm kiếm thông tin và giải đáp thắc mắc.",
    instruction=prompt.QA_AGENT_PROMPT
)
