from google.adk.agents import Agent
from . import prompt
from .sub_agents.coding_agent.agent import coding_agent
from .sub_agents.general_agent.agent import general_agent
from .sub_agents.QA_agent.agent import qa_agent
from .sub_agents.admission_agent.agent import admission_agent
from .sub_agents.learning_agent.agent import learning_agent

MODEL = "gemini-2.0-flash"
root_agent = Agent(
    name="root_agent",
    model=MODEL,
    description="Bộ điều phối chính, phân tích yêu cầu của người dùng và định tuyến đến agent chuyên biệt phù hợp nhất để xử lý.",
    instruction= prompt.ROOT_AGENT_PROMPT,
    sub_agents= [coding_agent, general_agent, qa_agent, admission_agent, learning_agent]
)