from core.runtime.file_explorer import FileExplorer


explorer = FileExplorer()


result = explorer.scan(
    "workspace/generated/generated_app"
)


print("PROJECT")
print(result["project"])


print("\nFILES")


for file in result["files"]:
    print(
        file["path"]
    )


print(
    "\nTOTAL:",
    result["count"]
)