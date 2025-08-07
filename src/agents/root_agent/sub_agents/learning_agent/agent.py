from google.adk.agents import Agent
from . import prompt, tools

MODEL = "gemini-2.0-flash"
learning_agent = Agent(
    name="learning_agent",
    model=MODEL,
    description="Giải quyết các câu hỏi và giải thích các khái niệm, lý thuyết, mô hình chuyên sâu thuộc các môn học ở bậc đại học, từ khoa học cơ bản đến các chuyên ngành kỹ thuật, kinh tế và xã hội.",
    instruction=prompt.LEARNING_AGENT_PROMPT
)
