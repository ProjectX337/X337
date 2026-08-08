import json
from pathlib import Path


class RuntimeRegistry:

    def __init__(
        self,
        storage_path="workspace/runtime/runtime_sessions.json"
    ):

        self.storage_path = Path(
            storage_path
        )

        self.sessions = {}

        self._load()



    #
    # Load persisted runtimes
    #
    def _load(
        self
    ):

        if self.storage_path.exists():

            try:

                self.sessions = json.loads(
                    self.storage_path.read_text()
                )

            except Exception:

                self.sessions = {}

        else:

            self.sessions = {}



    #
    # Save runtime state
    #
    def _save(
        self
    ):

        self.storage_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        self.storage_path.write_text(
            json.dumps(
                self.sessions,
                indent=2
            )
        )



    #
    # Register runtime session
    #
    def register(
        self,
        session
    ):

        #
        # Prevent duplicate artifact runtimes
        #
        existing_id = None


        for session_id, existing in self.sessions.items():

            if existing.get(
                "name"
            ) == session.name:

                existing_id = session_id
                break



        if existing_id:

            del self.sessions[
                existing_id
            ]



        #
        # Store newest session
        #
        self.sessions[
            session.id
        ] = session.to_dict()



        self._save()



    #
    # Find runtime by artifact name
    #
    def find_by_name(
        self,
        name
    ):

        for session in self.sessions.values():

            if session.get(
                "name"
            ) == name:

                return session


        return None



    #
    # Get runtime session
    #
    def get(
        self,
        name
    ):

        return self.find_by_name(
            name
        )



    #
    # Remove runtime by name
    #
    def remove_by_name(
        self,
        name
    ):

        remove_ids = []


        for session_id, session in self.sessions.items():

            if session.get(
                "name"
            ) == name:

                remove_ids.append(
                    session_id
                )



        for session_id in remove_ids:

            del self.sessions[
                session_id
            ]



        self._save()



    #
    # Update runtime status
    #
    def update_status(
        self,
        name,
        status
    ):

        session = self.find_by_name(
            name
        )


        if session:

            session[
                "status"
            ] = status


            self._save()



    #
    # Update health information
    #
    def update_health(
        self,
        name,
        healthy
    ):

        session = self.find_by_name(
            name
        )


        if session:

            session[
                "health"
            ] = {

                "status":
                    "healthy"
                    if healthy
                    else "unhealthy"

            }


            self._save()



    #
    # List all runtimes
    #
    def list(
        self
    ):

        return list(
            self.sessions.values()
        )
