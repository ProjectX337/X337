from pathlib import Path

from core.components.behavior_engine import (
    BehaviorEngine
)



class ComponentGenerator:


    def __init__(self):

        self.behavior_engine = (
            BehaviorEngine()
        )



    def generate(
        self,
        component,
        output_path
    ):


        filename = (
            output_path /
            f"{component.name}.tsx"
        )


        behavior = (
            self.behavior_engine.generate(
                component
            )
        )



        props = ""


        for prop in component.props:

            props += (
                f"""
{prop}: string;
"""
            )



        jsx = f"""

<div className="{component.name}">

<h2>
{component.name}
</h2>


<p>
{component.description}
</p>


</div>

"""



        content = f"""

{behavior["imports"]}


interface {component.name}Props {{

{props}

}}



export default function {component.name}(

props: {component.name}Props

) {{



{behavior["state"]}



{behavior["events"]}



return (

{jsx}

)


}}

"""



        filename.write_text(
            content
        )


        return str(filename)