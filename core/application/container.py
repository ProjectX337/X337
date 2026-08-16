from core.runtime.runtime_container import runtime_service
from core.agent.chat_agent import ChatAgent

chat_agent = ChatAgent(
    runtime_service=runtime_service,
)
