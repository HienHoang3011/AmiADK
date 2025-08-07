from google.adk.agents import Agent
from . import prompt, tools

MODEL = "gemini-2.0-flash"
coding_agent = Agent(
    name="coding_agent",
    model=MODEL,
    description="Viết, giải thích, sửa lỗi và tối ưu hóa code theo yêu cầu của người dùng trong nhiều ngôn ngữ lập trình khác nhau.",
    instruction=prompt.CODING_AGENT_PROMPT
)
