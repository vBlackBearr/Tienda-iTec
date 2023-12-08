from reactpy import component, html, use_state
from reactpy.core.hooks import use_context

# content
from admin.content.cruds.views.salesCrud import SalesCrud
from admin.content.screens._base import Base


@component
def Management(context):
    context_value = use_context(context)


    def UpdateForm():
        # Estados para almacenar los valores de los inputs
        input1_value, set_input1_value = use_state("")
        input2_value, set_input2_value = use_state("")

        # Función para manejar el evento de cambio en el primer input
        def handle_input1_change(e):
            set_input1_value(e["target"]["value"])

        # Función para manejar el evento de cambio en el segundo input
        def handle_input2_change(e):
            set_input2_value(e["target"]["value"])

        # Función para manejar el evento de clic en el botón "Update"
        def handle_update_click(e):
            # Aquí puedes realizar la lógica de actualización con los valores de los inputs
            print(f"Input 1: {input1_value}, Input 2: {input2_value}")

            # Puedes agregar aquí la lógica de actualización que necesitas

            # Limpia los valores de los inputs después de la actualización
            set_input1_value("")
            set_input2_value("")

        # Renderiza el formulario
        return html.div(
            {
                "style": {
                    "display": "flex",
                    "flex-direction": "row",
                    "gap": "30px",
                    # "width": "100px",
                    # "background-color": "black"
                }
            },
            html.label({"for": "input1"}, "Provider 1 endpoint:"),
            html.input({
                "type": "text",
                "id": "input1",
                "value": "https://example.prov1.com",
                "on_change": handle_input1_change,
            }),

            html.label({"for": "input2"}, "Provider 2 endpoint:"),
            html.input({
                "type": "text",
                "id": "input2",
                "value": "https://example.prov2.com",
                "on_change": handle_input2_change,
            }),

            html.button({
                "type": "button",
                "on_click": handle_update_click,
            }, "Update"),


        )

    def RP():
        # Estados para almacenar los valores de los inputs
        input1_value, set_input1_value = use_state("")
        input2_value, set_input2_value = use_state("")

        # Función para manejar el evento de cambio en el primer input
        def handle_input1_change(e):
            set_input1_value(e["target"]["value"])

        # Función para manejar el evento de cambio en el segundo input
        def handle_input2_change(e):
            set_input2_value(e["target"]["value"])

        # Función para manejar el evento de clic en el botón "Update"
        def handle_update_click(e):
            # Aquí puedes realizar la lógica de actualización con los valores de los inputs
            print(f"Input 1: {input1_value}, Input 2: {input2_value}")

            # Puedes agregar aquí la lógica de actualización que necesitas

            # Limpia los valores de los inputs después de la actualización
            set_input1_value("")
            set_input2_value("")

        # Renderiza el formulario
        return html.div(
            {
                "style": {
                    "display": "flex",
                    "flex-direction": "row",
                    "gap": "30px",
                    "margin-top": "40"
                    # "width": "100px",
                    # "background-color": "black"
                }
            },


            html.label({"for": "input2"}, "Min quantity for RP:"),
            html.input({
                "type": "text",
                "id": "input2",
                "value": "12345",
                "on_change": handle_input2_change,
            }),

            html.button({
                "type": "button",
                "on_click": handle_update_click,
            }, "Update"),
        )

    return Base((

        UpdateForm(),
        RP(),

    ), context_value)
