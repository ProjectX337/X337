from core.runtime.preview_registry import PreviewRegistry


registry = PreviewRegistry()


registry.register(
    "ai_tutor",
    "http://localhost:8000",
    8000,
    12345
)


print(
    registry.get(
        "ai_tutor"
    )
)


print(
    registry.list()
)
