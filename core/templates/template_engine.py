from core.templates.template_registry import (
    TemplateRegistry
)


class TemplateEngine:


    def __init__(self):

        self.registry = TemplateRegistry()



    def select_template(
        self,
        features
    ):

        best_template = None

        best_score = 0


        for template in self.registry.list():

            score = 0


            for feature in features:

                if feature in template.features:

                    score += 1


            if score > best_score:

                best_score = score

                best_template = template


        return best_template
