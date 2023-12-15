from reactpy import component, html, use_context, use_state

from admin.content.api import postPartner, postUser
from admin.content.screens._base import Base
from api_db.cruds.controllers.controllerPartners import create_partner
from api_db.cruds.controllers.controllerUsers import create_user
from api_db.cruds.schemas.schemas import UserCreate


@component
def AddPartner(context):
    context_value = use_context(context)

    # Definir el estado para cada campo del formulario
    name, set_name = use_state("")
    details, set_details = use_state("")
    direction, set_direction = use_state("")
    api_endpoint, set_api_endpoint = use_state("")

    # Manejar la creación del partner cuando se hace clic en el botón
    async def handleCreatePartner(e):

        # Crear un objeto con la información del nuevo partner

        new_user = {
            "username": name,
            "password": "",
            "email": "",
            "role_id": 4,
            "enabled": 1,
            "props": {},
        }

        user = await postUser(new_user)
        # print(user)
        new_partner = {
            "name": name,
            "details": details,
            "direction": direction,
            "api_endpoint": api_endpoint,
            "enabled": 1,
            "props": {},
            "user_id": user["data"]["id"],
        }

        await postPartner(new_partner)

        # Limpiar los campos del formulario después de la creación del partner
        set_name("")
        set_details("")
        set_direction("")
        set_api_endpoint("")

    return (
        Base((
            html.div(
                {"class": "container mt-5"},
                html.h2("Agregar Nuevo Partner"),
                html.form(
                    {},
                    html.div(
                        {"class": "form-group"},
                        html.label({"for": "name"}, "Nombre:"),
                        html.input(
                            {"type": "text", "class": "form-control", "id": "name", "name": "name", "required": True,
                             "value": name, "onChange": lambda e: set_name(e["target"]["value"])}),
                    ),
                    html.div(
                        {"class": "form-group"},
                        html.label({"for": "details"}, "Detalles:"),
                        html.input(
                            {"type": "text", "class": "form-control", "id": "details", "name": "details",
                             "value": details,
                             "onChange": lambda e: set_details(e["target"]["value"])}),
                    ),
                    html.div(
                        {"class": "form-group"},
                        html.label({"for": "direction"}, "Dirección:"),
                        html.input(
                            {"type": "text", "class": "form-control", "id": "direction", "name": "direction",
                             "value": direction, "onChange": lambda e: set_direction(e["target"]["value"])}),
                    ),
                    html.div(
                        {"class": "form-group"},
                        html.label({"for": "api_endpoint"}, "API Endpoint:"),
                        html.input(
                            {"type": "text", "class": "form-control", "id": "api_endpoint", "name": "api_endpoint",
                             "required": True, "value": api_endpoint,
                             "onChange": lambda e: set_api_endpoint(e["target"]["value"])}),
                    ),

                ),
                html.button({"on_click": handleCreatePartner, "class": "btn btn-primary"}, "Agregar Partner"),
            )
        ),
            context_value
        )
    )
