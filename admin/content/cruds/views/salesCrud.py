from reactpy import component, html, use_state, use_effect
import reactpy
import asyncio
from admin.content.api import getSales, postSale, deleteSale, updateSale, getUsers, getSaleStates

@component
def SalesCrud():
    sales, set_sales = use_state([])
    date, set_date = use_state("")
    total, set_total = use_state("")
    user_id, set_user_id = use_state("")  # Agrega este estado para almacenar el ID del usuario
    state_id, set_state_id = use_state("")  # Agrega este estado para almacenar el ID del estado
    editing, set_editing = use_state(False)
    sale_id, set_sale_id = use_state(None)

    dropdown_option, set_dropdown_option = use_state(None)
    users, set_users = use_state([])  # Estado para almacenar la lista de usuarios
    sale_states, set_sale_states = use_state([])  # Estado para almacenar la lista de estados de ventas

    # Llena la lista de usuarios y estados de ventas al cargar el componente
    # async def fillDropdownData():
    #     users_data = await getUsers()
    #     set_users(users_data)
    #
    #     states_data = await getSaleStates()
    #     set_sale_states(states_data)
    #
    # use_effect(fillDropdownData)

    async def fillItems():
        sales_data = await getSales()
        set_sales(sales_data)

    use_effect(fillItems)

    @reactpy.event(prevent_default=True)
    async def handle_submit(e):
        if not date or not total or not user_id or not state_id:
            return

        if not editing:
            new_sale = {
                "date": date,
                "total": total,
                "user_id": user_id,
                "state_id": state_id,
            }
            await postSale(new_sale)
            await fillItems()
        else:
            updated_sale = {
                "date": date,
                "total": total,
                "user_id": user_id,
                "state_id": state_id,
                "id": sale_id
            }
            await updateSale(sale_id, updated_sale)
            await fillItems()

        set_date("")
        set_total("")
        set_user_id("")
        set_state_id("")
        set_editing(False)
        set_sale_id(None)

    async def handle_delete(sale):
        await deleteSale(sale)
        await fillItems()

    async def handle_edit(sale):
        set_editing(True)
        set_date(sale["date"])
        set_total(sale["total"])
        set_user_id(sale["user_id"])
        set_state_id(sale["state_id"])
        set_sale_id(sale["id"])

    def delete_button_click_handler(e, sale_id):
        async def async_handler():
            await handle_delete(sale_id)

        asyncio.ensure_future(async_handler())

    def edit_button_click_handler(e, sale):
        async def async_handler():
            await handle_edit(sale)

        asyncio.ensure_future(async_handler())

    # Nueva función para obtener el nombre del usuario
    def get_user_name(user_id):
        user = next((user for user in users if user["id"] == user_id), None)
        return user["username"] if user else ""

    # Nueva función para obtener el nombre del estado de venta
    def get_sale_state_name(state_id):
        state = next((state for state in sale_states if state["id"] == state_id), None)
        return state["name"] if state else ""

    def create_table_row(sale):
        return html.tr(
            html.td(str(sale['date'])),
            html.td(str(sale['total'])),
            html.td(get_user_name(sale['user_id'])),  # Muestra el nombre del usuario
            html.td(get_sale_state_name(sale['state_id'])),  # Muestra el nombre del estado de venta
            html.td(
                html.div(
                    {"class": "dropdown"},
                    html.button(
                        {"class": "btn btn-secondary dropdown-toggle", "type": "button", "id": "dropdownMenuButton",
                         "data-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"},
                        "Actions"
                    ),
                    html.div(
                        {"class": "dropdown-menu", "aria-labelledby": "dropdownMenuButton"},
                        html.a(
                            {"class": "dropdown-item",
                             "on_click": lambda e, sale_id=sale["id"]: delete_button_click_handler(e, sale_id)},
                            "Delete"
                        ),
                        html.a(
                            {"class": "dropdown-item",
                             "on_click": lambda e, sale=sale: edit_button_click_handler(e, sale)},
                            "Edit"
                        )
                    )
                )
            )
        )

    list_items = html.div(
        {"class": "card shadow mb-4",
         "style": {
             "height": "400px"
         }
         },
        html.div(
            {"class": "card-header py-3"},
            html.h6({"class": "m-0 font-weight-bold text-primary"}, "Sales Example"),
        ),
        html.div(
            {"class": "card-body"},
            html.div(
                {"class": "table-responsive h-100",
                 "style": {
                 }},
                html.table(
                    {"class": "table table-bordered", "id": "dataTable", "width": "100%", "cellspacing": "0"},
                    html.thead(
                        html.tr(
                            html.th("Date"),
                            html.th("Total"),
                            html.th("User"),
                            html.th("State"),
                            html.th(""),
                        ),
                    ),
                    html.tbody(
                        [create_table_row(row) for row in sales]
                    ),
                ),
            ),
        ),
    )

    filters = html.div(
        {"class": "mb-4"},
        html.label({"class": "mr-2"}, "Filter by Enabled:"),
        html.select(
            {"class": "form-control", "on_change": lambda e: set_dropdown_option(e["target"]["value"])},
            html.option({"value": ""}, "All"),
            html.option({"value": "true"}, "Enabled"),
            html.option({"value": "false"}, "Disabled"),
        )
    )

    return html.div(
        {
            "style": {
                "padding": "3rem",
            }
        },
        filters,
        list_items,
        html.form(
            {
                "on_submit": handle_submit
            },
            html.input({
                "type": "date",
                "placeholder": "Date",
                "on_change": lambda e: set_date(e["target"]["value"]),
                "autofocus": True,
                "value": date,
                "class_name": "form-control mb-2"
            }),
            html.input({
                "type": "text",
                "placeholder": "Total",
                "on_change": lambda e: set_total(e["target"]["value"]),
                "value": total,
                "class_name": "form-control mb-2"
            }),
            html.select(
                {"class": "form-control mb-2", "on_change": lambda e: set_user_id(e["target"]["value"])},
                html.option({"value": ""}, "Select User"),
                [html.option({"value": user["id"]}, user["username"]) for user in users]
            ),
            html.select(
                {"class": "form-control mb-2", "on_change": lambda e: set_state_id(e["target"]["value"])},
                html.option({"value": ""}, "Select State"),
                [html.option({"value": state["id"]}, state["name"]) for state in sale_states]
            ),
            html.button({
                "type": "submit",
                "class_name": "btn btn-primary btn-block"
            }, "Create" if not editing else "Update"),
        ),
    )
