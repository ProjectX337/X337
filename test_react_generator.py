from core.templates.template_registry import TemplateRegistry
from core.templates.template_composer import TemplateComposer
from core.generator.react_generator import ReactGenerator


registry = TemplateRegistry()

template = registry.get(
    "ai_tutor"
)


composer = TemplateComposer()

blueprint = composer.compose(
    template
)


generator = ReactGenerator()


result = generator.generate(
    blueprint
)


print(result)