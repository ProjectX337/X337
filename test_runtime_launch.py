from core.runtime.manifest_loader import ManifestLoader


loader = ManifestLoader()

print(
    loader.list_manifests()
)


artifact = loader.load(
    "create_ai_tutor_website"
)


print(artifact)

print(
    artifact.run_commands
)
