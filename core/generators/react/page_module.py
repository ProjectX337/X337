from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule
from core.generators.react.layout_renderer import LayoutRenderer
from core.generators.react.page_naming import page_filename


class PageModule(BaseModule):
    """
    Generates React pages from canonical UISpec.page_models.

    UIPage is the sole frontend page contract.

    Feature-owned pages are placed under:
        frontend/src/features/<feature>/pages/

    Global pages are placed under:
        frontend/src/pages/
    """

    @property
    def name(self) -> str:
        return "pages"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:
        ui_spec = context.spec.ui_spec

        if not ui_spec:
            return

        renderer = LayoutRenderer()

        canonical_components = {
            component.name.lower().strip(): component
            for component in ui_spec.component_models
        }

        def collect_composition_components(node, names):
            if node is None:
                return

            if node.component is not None:
                names.add(
                    node.component.name
                )

            for child in node.children:
                collect_composition_components(
                    child,
                    names,
                )

        for page in ui_spec.page_models:
            feature_slug = page.metadata.get("feature")

            component_names = {
                component.name
                for component in page.components
            }

            collect_composition_components(
                page.composition,
                component_names,
            )

            component_imports = []

            for component_name in sorted(component_names):
                component = canonical_components.get(
                    component_name.lower().strip()
                )

                if component is None:
                    continue

                component_features = sorted(
                    set(
                        component.metadata.get(
                            "features",
                            [],
                        )
                    )
                )

                component_filename = page_filename(
                    component.name
                )

                if feature_slug:
                    if len(component_features) == 1:
                        if component_features[0] == feature_slug:
                            import_path = (
                                f"../components/"
                                f"{component_filename}"
                            )
                        else:
                            import_path = (
                                f"../../../features/"
                                f"{component_features[0]}/components/"
                                f"{component_filename}"
                            )
                    else:
                        import_path = (
                            f"../../../components/"
                            f"{component_filename}"
                        )
                else:
                    if len(component_features) == 1:
                        import_path = (
                            f"../features/"
                            f"{component_features[0]}/components/"
                            f"{component_filename}"
                        )
                    else:
                        import_path = (
                            f"../components/"
                            f"{component_filename}"
                        )

                component_imports.append(
                    {
                        "name": component.name,
                        "import_path": import_path,
                    }
                )

            if feature_slug:
                filename = page_filename(page.name)
                output = (
                    f"frontend/src/features/"
                    f"{feature_slug}/pages/"
                    f"{filename}.tsx"
                )
            else:
                # Preserve the existing global-page contract.
                output = f"frontend/src/pages/{page.name}.tsx"

            context.builder.template(
                template=(
                    "react/feature/page.tsx.j2"
                    if feature_slug
                    else "react/page.tsx.j2"
                ),
                output=output,
                language="typescript",
                feature=(
                    feature_slug
                    if feature_slug
                    else page.name
                ),
                page_name=page.name,
                route=page.route,
                components=page.components,
                component_imports=component_imports,
                metadata=page.metadata,
                composition=(
                    renderer.render(page.composition)
                    if page.composition
                    else ""
                ),
                page=page.name,
            )
