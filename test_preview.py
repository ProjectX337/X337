from core.runtime.preview_session import PreviewSession


preview = PreviewSession()


print(
    preview.wait_for_ready(8000)
)


print(
    preview.check_http(
        "http://localhost:8000"
    )
)
