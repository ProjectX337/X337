from core.runtime.app_explorer import AppExplorer


explorer = AppExplorer()


result = explorer.inspect(
    "generated_app"
)


print("\nAPPLICATION")
print(result["project"])


print("\nTOTAL FILES")
print(result["count"])


print("\nFILES")


for file in result["files"]:

    print(
        file["type"],
        "->",
        file["path"]
    )