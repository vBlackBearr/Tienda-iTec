from reactpy import use_context, html, use_state, use_effect

from admin.content.api import getRawMaterialsFromPartners
from admin.content.screens._base import Base


def AddRawMaterial(context):
    context_value = use_context(context)

    raw_materials, set_raw_materials = use_state([])

    cantidad_inputs, set_cantidad_inputs = use_state({})

    async def fetch_raw_materials():
        print("Fetching raw materials")
        response = await getRawMaterialsFromPartners()
        set_raw_materials(response)

    use_effect(fetch_raw_materials, [])

    def handleCantidadChange(raw_material_id, e):
        cantidad_inputs_copy = cantidad_inputs.copy()
        cantidad_inputs_copy[raw_material_id] = e["target"]["value"]
        set_cantidad_inputs(cantidad_inputs_copy)

    def create_table_row(raw_material_data):
        raw_material = raw_material_data["product"]
        raw_material_id = raw_material['id']
        return html.tr(
            html.td(raw_material['name']),
            html.td(raw_material['description']),
            html.td(raw_material_data['partner_name']),
            html.td(
                html.button({
                    "type": "button",
                    "class_name": "btn btn-primary",
                    "on_click": lambda e: handleCantidadChange(raw_material_id, e),
                }, "Seleccionar")
            )
        )

    list_items = html.div(
        {"class": "card shadow mb-4", "style": {"height": "400px"}},
        html.div(
            {"class": "card-header py-3 d-flex flex-row"},
            html.h6({"class": "m-0 font-weight-bold text-primary"}, "Raw Materials Table"),
        ),
        html.div(
            {"class": "card-body"},
            html.div(
                {"class": "table-responsive h-100"},
                html.table(
                    {"class": "table table-bordered", "id": "rawMaterialsTable", "width": "100%", "cellspacing": "0"},
                    html.thead(
                        html.tr(
                            html.th("Name"),
                            html.th("Description"),
                            html.th("Cantidad"),
                        ),
                    ),
                    html.tbody(
                        [create_table_row(row) for row in raw_materials]
                    ),
                ),
            ),
        ),
    )

    return (
        Base((
            html.h1("Add Raw Material"),
            list_items,
        ), context_value)
    )
