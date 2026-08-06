from __future__ import annotations

from core.knowledge.technology_definition import TechnologyDefinition


NEXTJS = TechnologyDefinition(

    name="Next.js",

    category="frontend",

    best_for=[
        "marketing",
        "dashboard",
        "seo",
    ],

    strengths=[
        "SSR",
        "Server Components",
        "App Router",
        "Streaming",
    ],

    weaknesses=[
        "Server complexity",
    ],

    integrates_with=[
        "React",
        "Vercel",
    ],

    recommended_architectures=[
        "SSR",
    ],
)


REACT = TechnologyDefinition(

    name="React",

    category="frontend",

    best_for=[
        "spa",
        "dashboard",
    ],

    strengths=[
        "Components",
        "Hooks",
        "Ecosystem",
    ],

    integrates_with=[
        "Vite",
        "Next.js",
    ],

    recommended_architectures=[
        "SPA",
    ],
)


FASTAPI = TechnologyDefinition(

    name="FastAPI",

    category="backend",

    best_for=[
        "api",
        "ai",
    ],

    strengths=[
        "Async",
        "OpenAPI",
        "Performance",
    ],

    integrates_with=[
        "Postgres",
        "Redis",
    ],

    recommended_architectures=[
        "SPA",
        "SSR",
    ],
)


POSTGRES = TechnologyDefinition(

    name="PostgreSQL",

    category="database",

    best_for=[
        "relational",
        "analytics",
    ],

    strengths=[
        "Transactions",
        "JSONB",
        "Indexes",
    ],
)


TECHNOLOGIES = {
    "nextjs": NEXTJS,
    "react": REACT,
    "fastapi": FASTAPI,
    "postgres": POSTGRES,
}
