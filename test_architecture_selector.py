from core.planner.prompt_parser import PromptParser
from core.planner.intent_classifier import IntentClassifier
from core.planner.architecture_selector import ArchitectureSelector

parser = PromptParser()
classifier = IntentClassifier()
selector = ArchitectureSelector()

parsed = parser.parse(
    "Build a modern AI SaaS with authentication, PostgreSQL and dashboards."
)

intent = classifier.classify(parsed)

architectures = selector.select(intent)

for candidate in architectures:
    print(candidate.architecture.name, candidate.score)