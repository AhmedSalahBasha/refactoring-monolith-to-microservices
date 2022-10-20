from modules.persons.app.udaconnect.models import Person  # noqa
from modules.persons.app.udaconnect.schemas import PersonSchema  # noqa


def register_routes(api, app, root="api"):
    from modules.persons.app.udaconnect.controllers import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")
