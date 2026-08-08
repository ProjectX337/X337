from core.runtime.code_viewer import CodeViewer


viewer = CodeViewer()


result = viewer.get_file(

    "generated_app",

    "src/components/AIChat.tsx"

)


print("FILE")
print(
    result["file"]
)


print("\nLANGUAGE")
print(
    result["language"]
)


print("\nCODE")
print(
    result["content"]
)