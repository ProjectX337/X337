from core.generator.project_generator import ProjectGenerator


generator = ProjectGenerator()


project = {
    "project": "ADHD Learning Assistant"
}


result = generator.generate(project)


print("\nX337 FILE GENERATOR")
print("===================")

print(
    f"Project: {result['project']}"
)

print(
    f"Directory: {result['directory']}"
)

print("\nGenerated files:")

for file in result["files"]:
    print(
        f"  ✓ {file}"
    )
