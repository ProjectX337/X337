from core.templates.template_engine import TemplateEngine


engine = TemplateEngine()


template = engine.select_template(
    [
        "authentication",
        "ai_tutor",
        "analytics"
    ]
)


print(template)
