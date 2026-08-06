from __future__ import annotations

from core.capabilities.models import (
    Capability,
    ComponentTemplate,
    FeatureTemplate,
    PageTemplate,
)


def create_capability() -> Capability:
    return Capability(
        name="authentication",
        description="User authentication and authorization",
        keywords=[
            "login",
            "signin",
            "signup",
            "authentication",
            "auth",
            "jwt",
        ],
        technologies=[
            "jwt",
            "bcrypt",
        ],
        required_roles=[
            "backend",
        ],
        priority=100,
        features=[
            FeatureTemplate(
                name="Authentication",
                slug="authentication",
                description="User authentication flows",
                pages=[
                    PageTemplate(
                        name="Login",
                        components=["AuthForm"],
                    ),
                    PageTemplate(
                        name="Signup",
                        components=["AuthForm"],
                    ),
                ],
                components=[
                    ComponentTemplate("AuthForm"),
                    ComponentTemplate("UserMenu"),
                ],
                api_endpoints=[
                    "/api/auth/login",
                    "/api/auth/signup",
                ],
            )
        ],
    )
