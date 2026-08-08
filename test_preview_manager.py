from core.runtime.preview_manager import PreviewManager


manager = PreviewManager()


preview = manager.create_preview(
    project_name="generated_app",
    project_path=
    "workspace/generated/generated_app",
    port=8000
)


print("PREVIEW")
print(preview)
