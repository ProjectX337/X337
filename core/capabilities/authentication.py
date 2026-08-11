from __future__ import annotations

from core.capabilities.capability import Capability


def create_capability() -> Capability:
    return Capability(
        name="authentication",
        description="User authentication and authorization",
        keywords=[
            "auth",
            "authentication",
            "login",
            "signup",
            "register",
            "password",
            "user",
        ],
        technologies=[
            "jwt",
            "bcrypt",
        ],
        required_roles=[
            "backend",
        ],
        pages=[
            "Login",
            "Signup",
        ],
        components=[
            "AuthForm",
            "UserMenu",
        ],
        priority=100,
        confidence=1.0,
        metadata={
            "api_endpoints": [
                "/api/auth/login",
                "/api/auth/signup",
            ],
            "features": [
                {
                    "name": "Authentication",
                    "slug": "authentication",
                    "description": "User authentication flows",
                    "pages": [
                        "Login",
                        "Signup",
                    ],
                    "components": [
                        "AuthForm",
                        "UserMenu",
                    ],
                    "api_endpoints": [
                        "/api/auth/login",
                        "/api/auth/signup",
                    ],
                }
            ],
        },
    )
