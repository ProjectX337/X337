from core.planner.prompt_parser import PromptParser
from core.planner.intent_classifier import IntentClassifier
from core.planner.architecture_selector import ArchitectureSelector
from core.planner.stack_builder import StackBuilder

parser = PromptParser()
classifier = IntentClassifier()
selector = ArchitectureSelector()
builder = StackBuilder()

parsed = parser.parse(
    "Build a modern AI SaaS with authentication, PostgreSQL and dashboards."
)

intent = classifier.classify(parsed)

candidates = selector.select(intent)

stack = builder.build(
    candidates,
    intent,
)

print(stack)