from core.generators.file_builder import FileBuilder

builder = FileBuilder()

builder.template(

    template="react/package.json.j2",

    output="frontend/package.json",

    language="json",

    project_name="x337-demo",

)

result = builder.result()

for file in result.files:

    print()

    print(file.path)

    print("-" * 40)

    print(file.content)
