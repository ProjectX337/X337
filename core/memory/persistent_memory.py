import json
import os


class PersistentMemory:


    def __init__(
        self,
        file_path=None
    ):


        #
        # Store memory inside X337/memory
        #

        if file_path is None:

            base_dir = os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.abspath(__file__)
                    )
                )
            )


            memory_dir = os.path.join(
                base_dir,
                "memory"
            )


            os.makedirs(
                memory_dir,
                exist_ok=True
            )


            file_path = os.path.join(
                memory_dir,
                "memory.json"
            )


        self.file_path = file_path


        self.data = {}


        self.load()



    def load(
        self
    ):


        if os.path.exists(
            self.file_path
        ):


            try:

                with open(
                    self.file_path,
                    "r"
                ) as file:


                    self.data = json.load(
                        file
                    )


            except Exception:


                self.data = {}



    def save(
        self
    ):


        with open(
            self.file_path,
            "w"
        ) as file:


            json.dump(

                self.data,

                file,

                indent=4

            )



    def remember(
        self,
        key,
        value
    ):

        # Automatically serialize ProjectSpec/dataclasses
        if hasattr(value, 'as_dict') and callable(value.as_dict):
            value = value.as_dict()
        elif hasattr(value, 'to_dict') and callable(value.to_dict):
            value = value.to_dict()

        self.data[key] = value
        self.save()

    def recall(
        self,
        key,
        default=None
    ):

        return self.data.get(
            key,
            default
        )

    def all(
        self
    ):

        return self.data
