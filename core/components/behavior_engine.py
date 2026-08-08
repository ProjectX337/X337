from typing import List



class BehaviorEngine:
    """
    Generates React logic from component metadata.
    """


    def generate_imports(
        self,
        component
    ):

        imports = ""

        if component.state:

            imports += """
import React, {
    useState
} from "react";
"""

        else:

            imports += """
import React from "react";
"""


        for service in component.services:

            imports += (
                f"""
import {service}
from "../services/{service}";
"""
            )


        return imports



    #
    # Generate React state
    #
    def generate_state(
        self,
        component
    ):

        output = ""


        for item in component.state:

            setter = (
                "set" +
                item[0].upper()
                +
                item[1:]
            )


            output += f"""

const [
    {item},
    {setter}
] = useState([]);


"""


        return output



    #
    # Generate event functions
    #
    def generate_events(
        self,
        component
    ):

        output = ""


        for event in component.events:


            output += f"""

function {event}(){{

    console.log(
        "{event}"
    );

}}

"""


        return output



    #
    # Full behavior generation
    #
    def generate(
        self,
        component
    ):

        return {

            "imports":
                self.generate_imports(
                    component
                ),

            "state":
                self.generate_state(
                    component
                ),

            "events":
                self.generate_events(
                    component
                )

        }