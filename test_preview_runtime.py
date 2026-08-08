from core.preview.runtime import preview_runtime


project = "adhd_learning_assistant"

result = preview_runtime.start(
    project,
    port=9100
)

print("\nX337 PREVIEW RUNTIME")
print("--------------------")
print(f"Project: {result['project']}")
print(f"Status:  {result['status']}")
print(f"URL:     {result['url']}")
