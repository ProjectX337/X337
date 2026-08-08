from core.dashboard.code_routes import (
    list_files,
    read_file
)


PROJECT_PATH = (
    "workspace/generated/generated_app"
)


print("FILES")

files = list_files(
    PROJECT_PATH
)


for file in files[:20]:

    print(file)



print("\nCODE")


print(
    read_file(
        PROJECT_PATH,
        "src/components/AIChat.tsx"
    )
)
