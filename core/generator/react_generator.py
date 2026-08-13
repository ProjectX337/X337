from pathlib import Path
import json

from core.components.component_library import ComponentLibrary
from core.generator.component_generator import ComponentGenerator



class ReactGenerator:
    """
    Generates React + TypeScript applications
    from the canonical generation context.
    """


    def __init__(
        self,
        output_root="workspace/generated"
    ):

        self.output_root = Path(output_root)

        self.component_library = ComponentLibrary()

        self.component_generator = ComponentGenerator()



    #
    # Main generation entry
    #
    def generate(
        self,
        blueprint
    ):

        project_path = (
            self.output_root /
            blueprint.name
        )


        self.create_structure(
            project_path
        )


        self.generate_package_json(
            project_path
        )


        self.generate_vite_config(
            project_path
        )


        self.generate_main(
            project_path
        )


        self.generate_app(
            project_path,
            blueprint
        )


        self.generate_pages(
            project_path,
            blueprint
        )


        self.generate_components(
            project_path,
            blueprint
        )


        return {

            "project":
                blueprint.name,

            "path":
                str(project_path),

            "framework":
                "react-typescript",

            "status":
                "generated"

        }



    #
    # Create folders
    #
    def create_structure(
        self,
        path
    ):

        folders = [

            "src",

            "src/components",

            "src/pages",

            "src/layouts",

            "src/hooks",

            "src/services"

        ]


        for folder in folders:

            (
                path / folder
            ).mkdir(
                parents=True,
                exist_ok=True
            )



    #
    # package.json
    #
    def generate_package_json(
        self,
        path
    ):

        package = {

            "name":
                path.name,

            "private":
                True,

            "version":
                "0.0.1",

            "type":
                "module",

            "scripts":
            {

                "dev":
                    "vite",

                "build":
                    "vite build",

                "preview":
                    "vite preview"

            },

            "dependencies":
            {

                "react":
                    "latest",

                "react-dom":
                    "latest",

                "react-router-dom":
                    "latest"

            },

            "devDependencies":
            {

                "typescript":
                    "latest",

                "vite":
                    "latest",

                "@vitejs/plugin-react":
                    "latest"

            }

        }


        with open(
            path / "package.json",
            "w"
        ) as file:

            json.dump(
                package,
                file,
                indent=4
            )



    #
    # Vite config
    #
    def generate_vite_config(
        self,
        path
    ):

        content = """

import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";


export default defineConfig({

plugins:[
react()
]

});

"""

        (
            path /
            "vite.config.ts"
        ).write_text(
            content
        )



    #
    # main.tsx
    #
    def generate_main(
        self,
        path
    ):

        content = """

import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";


ReactDOM.createRoot(
document.getElementById("root")!
)
.render(

<React.StrictMode>

<App />

</React.StrictMode>

);

"""

        (
            path /
            "src/main.tsx"
        ).write_text(
            content
        )



    #
    # App router
    #
    def generate_app(
        self,
        path,
        blueprint
    ):

        imports = ""

        routes = ""


        for page in blueprint.pages:

            imports += (
                f'import {page.name} '
                f'from "./pages/{page.name}";\n'
            )


            routes += f"""

<Route
path="{page.route}"
element={{<{page.name}/>}}
/>

"""


        content = f"""

import {{

BrowserRouter,

Routes,

Route

}} from "react-router-dom";


{imports}


export default function App(){{


return (

<BrowserRouter>

<Routes>

{routes}

</Routes>

</BrowserRouter>

)

}}

"""


        (
            path /
            "src/App.tsx"
        ).write_text(
            content
        )



    #
    # Pages
    #
    def generate_pages(
        self,
        path,
        blueprint
    ):

        for page in blueprint.pages:


            imports = ""

            components = ""


            for component in page.components:


                imports += (

                    f'import {component} '
                    f'from "../components/{component}";\n'

                )


                components += f"""

<{component}/>

"""


            content = f"""

{imports}


export default function {page.name}(){{


return (

<div>

{components}

</div>

)

}}

"""


            (
                path /
                "src/pages" /
                f"{page.name}.tsx"
            ).write_text(
                content
            )



    #
    # Intelligent Components
    #
    def generate_components(
        self,
        path,
        blueprint
    ):

        generated=set()


        output = (
            path /
            "src/components"
        )


        for page in blueprint.pages:

            for component in page.components:


                if component in generated:

                    continue


                generated.add(component)


                definition = (
                    self.component_library
                    .get(component)
                )


                if definition:


                    self.component_generator.generate(
                        definition,
                        output
                    )


                else:


                    file = (
                        output /
                        f"{component}.tsx"
                    )


                    file.write_text(
f"""

export default function {component}(){{


return (

<div>

<h2>
{component}
</h2>


<p>
Generated by X337
</p>


</div>

)

}}

"""
                    )