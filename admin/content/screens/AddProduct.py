from reactpy import use_context, html, use_state, use_effect

from admin.content.api import getRawMaterials, postProduct, postBOM
from admin.content.screens._base import Base


def AddProduct(context):
    context_value = use_context(context)

    name, set_name = use_state("")
    description, set_description = use_state("")
    stock, set_stock = use_state("")
    price, set_price = use_state("")

    raw_materials, set_raw_materials = use_state([])

    cantidad_inputs, set_cantidad_inputs = use_state({})

    async def handleCreate(e):
        print("Adding product")

        insert_data = {
            "name": name,
            "description": description,
            "stock": stock,
            "price": price,
            "enabled": 1
        }

        product_response = await postProduct(insert_data)

        if product_response["status_code"] == 200:
            product_id = product_response["data"]["id"]

            if product_id:
                for raw_material_id, cantidad in cantidad_inputs.items():

                    bom_data = {
                        "product_id": product_id,
                        "raw_material_id": raw_material_id,
                        "quantity": cantidad,
                        "enabled": 1
                    }

                    await postBOM(bom_data)

            else:
                print("Error: No se pudo obtener el ID del nuevo producto.")
        else:
            print("Error: No se pudo crear el producto.")

    async def fetch_raw_materials():
        print("Fetching raw materials")
        response = await getRawMaterials()
        set_raw_materials(response)

    use_effect(fetch_raw_materials, [])

    def handleCantidadChange(raw_material_id, e):
        cantidad_inputs_copy = cantidad_inputs.copy()
        cantidad_inputs_copy[raw_material_id] = e["target"]["value"]
        set_cantidad_inputs(cantidad_inputs_copy)
        # print(cantidad_inputs_copy)

    def create_table_row(raw_material):
        raw_material_id = raw_material['id']
        cantidad_input_value = cantidad_inputs.get(raw_material_id, "")
        return html.tr(
            html.td(raw_material['name']),
            html.td(raw_material['description']),
            html.td(
                html.input({
                    "type": "number",
                    "value": cantidad_input_value,
                    "on_change": lambda e: handleCantidadChange(raw_material_id, e),
                    "class_name": "form-control",
                    "style": {
                        "width": "100px"
                    }
                })
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
                    {"class": "table table-bordered", "id": "dataTable", "width": "100%", "cellspacing": "0"},
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
            html.h1("Add New Product"),
            html.form(
                {},
                html.input({
                    "type": "text",
                    "placeholder": "Name",
                    "on_change": lambda e: set_name(e["target"]["value"]),
                    "autofocus": True,
                    "value": name,
                    "class_name": "form-control mb-2"
                }),
                html.input({
                    "type": "text",
                    "placeholder": "Description",
                    "on_change": lambda e: set_description(e["target"]["value"]),
                    "value": description,
                    "class_name": "form-control mb-2"
                }),
                html.input({
                    "type": "number",
                    "placeholder": "Initial stock",
                    "on_change": lambda e: set_stock(e["target"]["value"]),
                    "value": stock,
                    "class_name": "form-control mb-2"
                }),
                html.input({
                    "type": "number",
                    "placeholder": "Price",
                    "on_change": lambda e: set_price(e["target"]["value"]),
                    "value": price,
                    "class_name": "form-control mb-2"
                }),
                list_items,

            ),
            html.button({
                "on_click": handleCreate,
                "class_name": "btn btn-primary btn-block"
            }, "Create"),
        ), context_value)
    )
