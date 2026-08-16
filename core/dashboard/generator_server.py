from __future__ import annotations

import json
import re
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

from core.agent.change_engine import ChangeEngine
from core.generators.generation_service import GenerationService
from core.generators.result_writer import ResultWriter
from core.planner.project_planner import ProjectPlanner
from core.training.training_store import TrainingStore
from core.application.container import chat_agent


TRAINING_PATH = Path(
    "workspace/training/examples.json"
)

OUTPUT_ROOT = Path(
    "workspace/generated"
)


planner = ProjectPlanner()
change_engine = ChangeEngine()
generation_service = GenerationService()


writer = ResultWriter()

training_store = TrainingStore()


def safe_slug(value: str) -> str:
    value = value.strip().lower()

    value = re.sub(
        r"[^a-z0-9]+",
        "-",
        value,
    )

    return value.strip("-") or "x337-app"


def load_training_examples() -> list[dict]:
    return training_store.list()


def relevant_training_profiles(
    prompt: str,
) -> list[dict]:
    prompt_lower = prompt.lower()

    scored = []

    for example in training_store.list():
        profile = example.get("profile", {})

        score = 0

        for keyword in profile.get(
            "keywords",
            [],
        ):
            if keyword.lower() in prompt_lower:
                score += 3

        for pattern in profile.get(
            "layout_patterns",
            [],
        ):
            if pattern.lower() in prompt_lower:
                score += 2

        if profile.get("visual_style"):
            score += 1

        if score:
            scored.append(
                (
                    score,
                    example,
                )
            )

    scored.sort(
        key=lambda item: item[0],
        reverse=True,
    )

    return [
        example
        for _score, example
        in scored[:5]
    ]



def apply_training_profile(
    spec,
    examples: list[dict],
) -> None:
    """
    Apply learned design intelligence to the canonical DesignSystem.

    Training changes design tokens and semantic visual intent rather
    than copying reference source code into generated applications.
    """

    if not examples:
        return

    ui_spec = getattr(spec, "ui_spec", None)

    if ui_spec is None:
        return

    design_system = getattr(
        ui_spec,
        "design_system",
        None,
    )

    if design_system is None:
        return

    profiles = [
        example.get("profile", {})
        for example in examples
        if example.get("profile")
    ]

    if not profiles:
        return

    def unique(values):
        return list(
            dict.fromkeys(
                value
                for value in values
                if value
            )
        )

    colors = unique(
        color
        for profile in profiles
        for color in profile.get("colors", [])
    )

    fonts = unique(
        font
        for profile in profiles
        for font in profile.get("fonts", [])
    )

    spacing_values = unique(
        value
        for profile in profiles
        for value in profile.get(
            "spacing_values",
            [],
        )
    )

    spacing_roles = {
        "compact": unique(
            value
            for profile in profiles
            for value in profile.get(
                "spacing_roles",
                {},
            ).get("compact", [])
        ),
        "comfortable": unique(
            value
            for profile in profiles
            for value in profile.get(
                "spacing_roles",
                {},
            ).get("comfortable", [])
        ),
        "spacious": unique(
            value
            for profile in profiles
            for value in profile.get(
                "spacing_roles",
                {},
            ).get("spacious", [])
        ),
    }

    layout_patterns = unique(
        pattern
        for profile in profiles
        for pattern in profile.get(
            "layout_patterns",
            [],
        )
    )

    component_patterns = unique(
        pattern
        for profile in profiles
        for pattern in profile.get(
            "component_patterns",
            [],
        )
    )


    # ---------------------------------------------------------
    # Learned component intelligence -> component metadata
    # ---------------------------------------------------------

    component_roles = {}

    for profile in profiles:
        for name, data in profile.get(
            "component_roles",
            {},
        ).items():
            component_roles[name] = data

    if component_roles and spec.ui_spec:

        for component in spec.ui_spec.component_models:

            learned = component_roles.get(
                component.name
            )

            if not learned:
                continue

            component.metadata[
                "training_role"
            ] = learned.get(
                "role",
                "",
            )

            component.metadata[
                "training_patterns"
            ] = learned.get(
                "patterns",
                [],
            )

    interaction_patterns = unique(
        pattern
        for profile in profiles
        for pattern in profile.get(
            "interaction_patterns",
            [],
        )
    )

    keywords = unique(
        keyword
        for profile in profiles
        for keyword in profile.get(
            "keywords",
            [],
        )
    )

    # ---------------------------------------------------------
    # Learned visual identity
    # ---------------------------------------------------------

    if hasattr(design_system, "visual_style"):
        styles = []

        for profile in profiles:
            style = profile.get(
                "visual_style",
                "",
            )

            if style:
                styles.append(style)

        if styles:
            design_system.visual_style = " ".join(
                unique(styles)
            )

    # ---------------------------------------------------------
    # Learned colors -> canonical semantic tokens
    # ---------------------------------------------------------

    if colors and hasattr(
        design_system,
        "colors",
    ):
        existing = dict(
            getattr(
                design_system,
                "colors",
                {},
            ) or {}
        )

        semantic_roles = {}

        for profile in profiles:
            for role, values in profile.get(
                "color_roles",
                {},
            ).items():
                semantic_roles.setdefault(
                    role,
                    [],
                ).extend(values)

        semantic_role_names = (
            "background",
            "surface",
            "primary",
            "secondary",
            "accent",
            "text",
            "muted",
        )

        has_semantic_roles = any(
            semantic_roles.get(role)
            for role in semantic_role_names
        )

        if has_semantic_roles:
            for role in semantic_role_names:
                values = unique(
                    semantic_roles.get(
                        role,
                        [],
                    )
                )

                if values:
                    existing[role] = values[0]

            # A learned border is retained when supported.
            if semantic_roles.get("border"):
                existing.setdefault(
                    "border",
                    unique(
                        semantic_roles["border"]
                    )[0],
                )

        else:
            # Backward-compatible path for older training records
            # that only contain the ordered colors list.
            legacy_roles = (
                "background",
                "surface",
                "primary",
                "secondary",
                "accent",
                "text",
                "muted",
            )

            for index, color in enumerate(
                colors[:len(legacy_roles)]
            ):
                existing[
                    legacy_roles[index]
                ] = color

        design_system.colors = existing

        if hasattr(
            design_system,
            "color_palette",
        ):
            existing_palette = list(
                getattr(
                    design_system,
                    "color_palette",
                    [],
                ) or []
            )

            design_system.color_palette = unique(
                colors + existing_palette
            )[:12]

    # ---------------------------------------------------------
    # Learned fonts -> canonical typography tokens
    # ---------------------------------------------------------

    if fonts and hasattr(
        design_system,
        "typography",
    ):
        typography = dict(
            getattr(
                design_system,
                "typography",
                {},
            ) or {}
        )

        typography["heading"] = fonts[0]
        typography["body"] = fonts[0]

        if len(fonts) > 1:
            typography["mono"] = fonts[-1]

        design_system.typography = typography

    # ---------------------------------------------------------
    # Learned spacing -> canonical spacing tokens
    # ---------------------------------------------------------

    if spacing_values and hasattr(
        design_system,
        "spacing",
    ):
        spacing = dict(
            getattr(
                design_system,
                "spacing",
                {},
            ) or {}
        )

        compact = spacing_roles["compact"]
        comfortable = spacing_roles["comfortable"]
        spacious = spacing_roles["spacious"]

        def numeric(value: str) -> float:
            import re

            match = re.search(
                r"-?\d+(?:\.\d+)?",
                str(value),
            )

            return (
                float(match.group(0))
                if match
                else 0.0
            )

        if compact:
            spacing["unit"] = min(
                compact,
                key=numeric,
            )

        elif spacing_values:
            spacing["unit"] = min(
                spacing_values,
                key=numeric,
            )

        if comfortable:
            spacing["section"] = max(
                comfortable,
                key=numeric,
            )

        elif len(spacing_values) >= 2:
            section_candidates = [
                value
                for value in spacing_values
                if numeric(value) <= 256
            ]

            if section_candidates:
                spacing["section"] = max(
                    section_candidates,
                    key=numeric,
                )
            else:
                spacing["section"] = spacing_values[1]

        if spacious:
            spacing["container"] = max(
                spacious,
                key=numeric,
            )

        elif len(spacing_values) >= 3:
            container_candidates = [
                value
                for value in spacing_values
                if numeric(value) > 256
            ]

            if container_candidates:
                spacing["container"] = max(
                    container_candidates,
                    key=numeric,
                )
            else:
                spacing["container"] = spacing_values[-1]

        design_system.spacing = spacing

        if hasattr(
            design_system,
            "metadata",
        ):
            design_system.metadata[
                "training_spacing_roles"
            ] = {
                "compact": compact,
                "comfortable": comfortable,
                "spacious": spacious,
            }

    # ---------------------------------------------------------
    # Learned semantic behavior
    # ---------------------------------------------------------

    if hasattr(
        design_system,
        "metadata",
    ):
        design_system.metadata["training_profile"] = {
            "examples_used": len(profiles),
            "colors": colors[:12],
            "fonts": fonts[:8],
            "spacing_values": spacing_values[:12],
            "layout_patterns": layout_patterns,
            "component_patterns": component_patterns,
            "interaction_patterns": interaction_patterns,
            "keywords": keywords,
        }


class GeneratorHandler(BaseHTTPRequestHandler):

    def _send_json_headers(self, status=200):
        self.send_response(status)

        self.send_header(
            "Content-Type",
            "application/json",
        )

        self.send_header(
            "Access-Control-Allow-Origin",
            "*",
        )

        self.send_header(
            "Access-Control-Allow-Methods",
            "GET, POST, OPTIONS",
        )

        self.send_header(
            "Access-Control-Allow-Headers",
            "Content-Type",
        )

        self.end_headers()

    def do_OPTIONS(self):
        self._send_json_headers()

    def do_GET(self):

        if self.path == "/api/training":
            examples = load_training_examples()

            self._send_json_headers()

            self.wfile.write(
                json.dumps(
                    {
                        "examples": examples,
                    }
                ).encode()
            )

            return

        self._send_json_headers(404)

        self.wfile.write(
            json.dumps(
                {
                    "error": "Endpoint not found",
                }
            ).encode()
        )

    def do_POST(self):

        if self.path == "/api/training":
            self.handle_training()
            return

        if self.path == "/api/generate":
            self.handle_generate()
            return

        if self.path == "/api/chat":
            self.handle_chat()
            return

        self._send_json_headers(404)

        self.wfile.write(
            json.dumps(
                {
                    "error": "Endpoint not found",
                }
            ).encode()
        )

    def read_json(self) -> dict:

        length = int(
            self.headers_value(
                "Content-Length",
                "0",
            )
        )

        body = self.rfile.read(length)

        return json.loads(
            body.decode("utf-8")
        )

    def headers_value(
        self,
        name: str,
        default: str,
    ) -> str:
        value = self.headers.get(name)

        if value is None:
            return default

        return value

    def handle_chat(self):

        try:
            data = self.read_json()

            message = str(
                data.get(
                    "message",
                    "",
                )
            ).strip()

            if not message:
                self._send_json_headers(400)

                self.wfile.write(
                    json.dumps(
                        {
                            "error": "Message is required",
                        }
                    ).encode()
                )

                return

            result = chat_agent.respond(
                message
            )

            self._send_json_headers()

            self.wfile.write(
                json.dumps(
                    result,
                    default=str,
                ).encode()
            )

        except Exception as error:

            self._send_json_headers(500)

            self.wfile.write(
                json.dumps(
                    {
                        "error": str(error),
                    }
                ).encode()
            )


    def handle_training(self):

        try:
            data = self.read_json()

            name = str(
                data.get(
                    "name",
                    "Reference",
                )
            ).strip()

            description = str(
                data.get(
                    "description",
                    "",
                )
            ).strip()

            code = str(
                data.get(
                    "code",
                    "",
                )
            )

            training_store.add(
                name=name,
                description=description,
                code=code,
            )

            examples = training_store.list()

            self._send_json_headers()

            self.wfile.write(
                json.dumps(
                    {
                        "status": "learned",
                        "training": examples[-1],
                        "examples": examples,
                    }
                ).encode()
            )

        except Exception as error:

            self._send_json_headers(500)

            self.wfile.write(
                json.dumps(
                    {
                        "error": str(error),
                    }
                ).encode()
            )

    def handle_generate(self):

        try:
            data = self.read_json()

            prompt = str(
                data.get(
                    "prompt",
                    "",
                )
            ).strip()

            if not prompt:
                self._send_json_headers(400)

                self.wfile.write(
                    json.dumps(
                        {
                            "error": "Prompt is required",
                        }
                    ).encode()
                )

                return

            # -------------------------------------------------
            # 1. Canonical planning
            # -------------------------------------------------

            spec = planner.plan(prompt)

            # -------------------------------------------------
            # 1b. Apply learned training intelligence
            # -------------------------------------------------

            learned_examples = (
                relevant_training_profiles(prompt)
            )

            apply_training_profile(
                spec,
                learned_examples,
            )

            # -------------------------------------------------
            # 2. Canonical change planning
            # -------------------------------------------------

            changes = []

            # -------------------------------------------------
            # 3. Canonical application generation
            # -------------------------------------------------

            result = generation_service.generate(
                spec
            )

            # -------------------------------------------------
            # 5. Persist generated application
            # -------------------------------------------------

            slug = safe_slug(
                spec.project_name
                or prompt
            )

            output_root = (
                OUTPUT_ROOT / slug
            )

            output_root.mkdir(
                parents=True,
                exist_ok=True,
            )

            writer.write(
                result,
                root=str(output_root),
            )

            # -------------------------------------------------
            # 5b. Start live generated-app preview
            # -------------------------------------------------

            preview = chat_agent.start_preview(
                slug
            )

            files = [
                file.path
                for file in result.files
            ]

            # -------------------------------------------------
            # 6. Return canonical application
            # -------------------------------------------------

            response = {
                "project": slug,
                "status": "generated",
                "directory": str(output_root),
                "files": files,
                "pages": [
                    page.name
                    for page in spec.ui_spec.page_models
                ],
                "components": [
                    component.name
                    for component
                    in spec.ui_spec.component_models
                ],
                "training_examples": len(
                    load_training_examples()
                ),
                "preview": {
                    "status": preview["status"],
                    "url": preview["url"],
                    "port": preview["port"],
                },
                "message": (
                    "X337 generated a canonical "
                    "React application"
                ),
            }

            self._send_json_headers()

            self.wfile.write(
                json.dumps(
                    response
                ).encode()
            )

        except Exception as error:

            self._send_json_headers(500)

            self.wfile.write(
                json.dumps(
                    {
                        "error": str(error),
                    }
                ).encode()
            )


def start_generator_server(
    host="127.0.0.1",
    port=9000,
):

    server = HTTPServer(
        (
            host,
            port,
        ),
        GeneratorHandler,
    )

    print(
        "X337 Generator Server running at "
        f"http://{host}:{port}"
    )

    server.serve_forever()


if __name__ == "__main__":
    start_generator_server()
