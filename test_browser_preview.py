from core.runtime.browser_preview import BrowserPreview
import time


preview = BrowserPreview()


result = preview.start(
    "workspace/generated/generated_app"
)


print("\nBROWSER PREVIEW")
print(result)


print("\nPreview running...")
print(result["url"])


time.sleep(60)


preview.stop()