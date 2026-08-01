from core.planner.stack_builder import ArchitectureStack
from core.planner.technology_resolver import TechnologyResolver


resolver = TechnologyResolver()

stack = ArchitectureStack(
    frontend="react",
    backend="fastapi",
    ai="ai_agent",
    scripting="python",
)

plan = resolver.resolve(stack)

print("Database:", plan.database)
print("ORM:", plan.orm)
print("Authentication:", plan.authentication)
print("Styling:", plan.styling)
print("Routing:", plan.routing)
print("State:", plan.state_management)
print("LLM:", plan.llm_provider)
print("Embeddings:", plan.embeddings)
print("Vector DB:", plan.vector_database)
print("Formatter:", plan.formatter)
print("Linter:", plan.linter)
print("Container:", plan.containerization)
print("Backend Package Manager:", plan.package_manager_backend)
print("Frontend Package Manager:", plan.package_manager_frontend)
