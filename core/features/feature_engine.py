from core.features.feature_schema import (
    FeatureBlueprint
)



class FeatureEngine:
    """
    Converts user requirements into
    application features.
    """


    def __init__(self):

        self.feature_library = {

            "ai_tutor":

            FeatureBlueprint(

                name="AI Tutor",

                category="education",

                pages=[

                    "Dashboard",

                    "Lesson",

                    "Profile"

                ],

                components=[

                    "AIChat",

                    "LessonCard",

                    "ProgressChart",

                    "ProfileCard"

                ],

                services=[

                    "aiTutorService",

                    "progressService"

                ],

                ai_capabilities=[

                    "conversation",

                    "personalization",

                    "lesson_support"

                ],

                analytics=[

                    "learning_progress",

                    "engagement"

                ]

            ),



            "dyslexia_support":

            FeatureBlueprint(

                name="Dyslexia Support",

                category="learning_support",

                pages=[

                    "ReadingCoach",

                    "Practice"

                ],


                components=[

                    "SpeechReader",

                    "ReadingExercise",

                    "VocabularyVisualizer"

                ],


                services=[

                    "speechService",

                    "readingService"

                ],


                ai_capabilities=[

                    "text_simplification",

                    "phonological_training"

                ]

            ),



            "adhd_support":

            FeatureBlueprint(

                name="ADHD Support",

                category="executive_function",

                pages=[

                    "Planner",

                    "Focus"

                ],


                components=[

                    "TaskPlanner",

                    "FocusTimer",

                    "ProgressTracker"

                ],


                services=[

                    "taskService"

                ],


                ai_capabilities=[

                    "task_breakdown",

                    "focus_coaching"

                ]

            )

        }



    def analyze(
        self,
        prompt: str
    ):


        prompt = (
            prompt.lower()
        )


        selected = []


        for key, feature in (
            self.feature_library.items()
        ):


            if key in prompt:

                selected.append(
                    feature
                )


            elif feature.name.lower() in prompt:

                selected.append(
                    feature
                )



        return selected