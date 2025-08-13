from google.adk.agents import Agent
import core
from .prompt import root_agent_instruction
from .sub_agents.general_agent.agent import general_agent
from dotenv import load_dotenv
from google.genai import types
from google.adk.planners import BuiltInPlanner

load_dotenv()

root_agent = Agent(
    name = "root_agent",
    model = core.THINKING_MODEL,
    description= "Tác nhân gốc, có chức năng phân tích và định tuyến yêu cầu đến tác nhân phù hợp.",
    instruction= root_agent_instruction,
    planner= BuiltInPlanner(
        thinking_config= types.ThinkingConfig(
            include_thoughts= True,
            thinking_budget= 1024
        )
    ),
    sub_agents= [general_agent]
)