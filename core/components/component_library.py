from pathlib import Path
import json

from core.components.component_schema import (
    ComponentDefinition
)



class ComponentLibrary:
    """
    Loads and manages the X337 component library.

    Component definitions live inside:

    core/components/definitions/*.json

    Example:

    AIChat.json
    Dashboard.json
    Navbar.json

    The library converts JSON definitions
    into ComponentDefinition objects.
    """


    def __init__(
        self,
        definition_path="core/components/definitions"
    ):

        self.definition_path = Path(
            definition_path
        )

        self.components = {}

        self.load_all()



    #
    # Load all component definitions
    #
    def load_all(
        self
    ):

        if not self.definition_path.exists():

            return


        allowed_fields = set(
            ComponentDefinition
            .__dataclass_fields__
            .keys()
        )


        for file in self.definition_path.glob(
            "*.json"
        ):


            try:

                data = json.loads(
                    file.read_text()
                )


            except Exception as error:

                print(
                    f"Failed loading {file}: {error}"
                )

                continue



            #
            # Ignore unknown future fields
            #
            clean_data = {

                key:value

                for key,value in data.items()

                if key in allowed_fields

            }



            try:

                component = (
                    ComponentDefinition(
                        **clean_data
                    )
                )


            except TypeError as error:

                print(
                    f"Invalid component {file}: {error}"
                )

                continue



            self.components[
                component.name
            ] = component



    #
    # Get component by name
    #
    def get(
        self,
        name
    ):

        return self.components.get(
            name
        )



    #
    # Check component exists
    #
    def exists(
        self,
        name
    ):

        return (
            name in self.components
        )



    #
    # List all components
    #
    def list(
        self
    ):

        return list(
            self.components.values()
        )



    #
    # Reload definitions
    #
    def reload(
        self
    ):

        self.components.clear()

        self.load_all()



    #
    # Search components
    #
    def search(
        self,
        category=None
    ):

        results = []


        for component in (
            self.components.values()
        ):


            if category:

                if (
                    component.category
                    != category
                ):

                    continue



            results.append(
                component
            )


        return results