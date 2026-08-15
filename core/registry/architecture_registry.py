from __future__ import annotations

from core.plugins.plugin_loader import PluginLoader
from core.registry.architecture import Architecture


class ArchitectureRegistry:
    """
    Central registry of every architecture
    supported by X337.
    """

    def __init__(self):

        self._architectures: dict[str, Architecture] = {}

        loader = PluginLoader()

        architectures = loader.load()

        if architectures:

            for architecture in architectures:
                self.register(architecture)

        else:

            self._register_defaults()

    # ---------------------------------------------------------

    def register(
        self,
        architecture: Architecture,
    ) -> None:

        self._architectures[
            architecture.name.lower()
        ] = architecture

    # ---------------------------------------------------------

    def get(
        self,
        name: str,
    ) -> Architecture:

        key = name.lower()

        if key not in self._architectures:

            raise KeyError(
                f"Unknown architecture: {name}"
            )

        return self._architectures[key]

    # ---------------------------------------------------------

    def exists(
        self,
        name: str,
    ) -> bool:

        return name.lower() in self._architectures

    def names(self) -> list[str]:

        return sorted(
            self._architectures.keys()
        )

    def all(self) -> list[Architecture]:

        return list(
            self._architectures.values()
        )

    # ---------------------------------------------------------
    # Built-in fallback
    # ---------------------------------------------------------

    def _register_defaults(self):

        self.register(
            Architecture(
                name="fastapi",
                language="python",
                template="fastapi",
                tester="pytest",
                keywords=[
                    "api",
                    "backend",
                    "rest",
                    "fastapi",
                ],
                dependencies=[
                    "fastapi",
                    "uvicorn",
                    "pydantic",
                ],
                default_features=[
                    "routes",
                    "schemas",
                    "services",
                    "tests",
                ],
                technology_defaults={
                    "database": "PostgreSQL",
                    "orm": "SQLAlchemy",
                    "api_style": "REST",
                    "validation": "Pydantic",
                    "package_manager_backend": "pip",
                },
            )
        )

        self.register(
            Architecture(
                name="react",
                language="javascript",
                template="react",
                tester="vitest",
                keywords=[
                    "react",
                    "frontend",
                    "spa",
                    "dashboard",
                    "ui",
                ],
                dependencies=[
                    "react",
                    "react-dom",
                    "vite",
                ],
                technology_defaults={
                    "styling": "tailwindcss",
                    "state_management": "zustand",
                    "routing": "react-router",
                    "ui_library": "shadcn",
                    "package_manager_frontend": "npm",
                },
            )
        )

        self.register(
            Architecture(
                name="website",
                language="html",
                template="website",
                tester="none",
                keywords=[
                    "website",
                    "landing",
                    "portfolio",
                    "business",
                ],
            )
        )

        self.register(
            Architecture(
                name="python",
                language="python",
                template="python",
                tester="pytest",
                keywords=[
                    "python",
                    "script",
                    "automation",
                ],
            )
        )

        self.register(
            Architecture(
                name="ai_agent",
                language="python",
                template="ai_agent",
                tester="pytest",
                keywords=[
                    "agent",
                    "assistant",
                    "llm",
                    "ai",
                ],
                technology_defaults={
                    "llm_provider": "OpenAI",
                    "vector_database": "pgvector",
                    "embeddings": "text-embedding",
                },
            )
        )