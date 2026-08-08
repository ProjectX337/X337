from dataclasses import dataclass, field


@dataclass
class PageBlueprint:
    name: str
    route: str
    components: list[str]


@dataclass
class ApplicationBlueprint:

    name: str

    pages: list[PageBlueprint] = field(
        default_factory=list
    )

    features: list[str] = field(
        default_factory=list
    )



class TemplateComposer:


    def compose(
        self,
        template
    ):

        pages=[]


        for page in template.pages:

            pages.append(
                PageBlueprint(
                    name=page,
                    route=self.route(page),
                    components=self.components_for(page)
                )
            )


        return ApplicationBlueprint(

            name=template.name,

            pages=pages,

            features=template.features

        )


    def route(
        self,
        page
    ):

        return (
            "/" 
            + page.lower()
        ).replace(
            "landing",
            ""
        ) or "/"


    def components_for(
        self,
        page
    ):

        mapping={

            "Landing":[
                "Navbar",
                "Hero",
                "FeatureGrid"
            ],

            "Dashboard":[
                "Navbar",
                "AIChat",
                "ProgressChart"
            ],

            "Lesson":[
                "LessonCard",
                "AIChat"
            ],

            "Profile":[
                "ProfileCard"
            ],

            "Login":[
                "LoginForm"
            ]

        }


        return mapping.get(
            page,
            []
        )