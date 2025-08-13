from google.adk.agents import Agent
import core
from google.adk.tools import google_search
from .prompt import general_agent_instruction, google_search_instruction
from google.adk.tools.agent_tool import AgentTool

google_search_agent = Agent(
    name = "google_search_agent",
    model = core.GENERAL_MODEL,
    description= "Một tác nhân chuyên trách thực hiện các tìm kiếm trên Google để thu thập thông tin.",
    instruction= google_search_instruction,
    tools = [google_search]
)
general_agent = Agent(
    name = "general_agent",
    model = core.GENERAL_MODEL,
    description= "Một tác nhân đa năng có khả năng xử lý các yêu cầu không chuyên biệt và cung cấp thông tin chung cho người dùng.",
    instruction= general_agent_instruction,
    tools = [AgentTool(agent= google_search_agent)]
)
