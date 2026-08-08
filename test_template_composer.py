from core.templates.template_registry import TemplateRegistry
from core.templates.template_composer import TemplateComposer


registry = TemplateRegistry()

template = registry.get(
    "ai_tutor"
)


composer = TemplateComposer()

app = composer.compose(template)


print(app)

for page in app.pages:
    print(
        page.name,
        page.route,
        page.components
    )