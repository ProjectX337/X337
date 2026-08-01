from core.templates.template_engine import TemplateEngine

engine = TemplateEngine()

result = engine.render(

    "react/package.json.j2",

    project_name="my-ai-app",

)

print(result)
