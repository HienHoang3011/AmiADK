from google.adk.models.lite_llm import LiteLlm

THINKING_MODEL = "gemini-2.5-flash" # Woking well with BuiltInPlanner
GENERAL_MODEL = "gemini-2.0-flash"
REASONING_MODEL = LiteLlm(model = "openai/gpt-4.1")
CODING_MODEL = LiteLlm(model="anthropic/claude-sonnet-4-20250514")