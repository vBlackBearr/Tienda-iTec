from reactpy import use_state, html, component

from static.api import updateCartQuantity, deleteProductFromCart


@component
def item(product, token, fetch_products):
    quantity, set_quantity = use_state(product['quantity'])

    async def increase_quantity(e):
        new_quantity = quantity + 1
        await updateCartQuantity(token, product["id"], new_quantity)
        set_quantity(new_quantity)
        await fetch_products()

    async def decrease_quantity(e):
        if quantity >= 2:
            new_quantity = quantity - 1
            await updateCartQuantity(token, product["id"], new_quantity)
            set_quantity(new_quantity)
            await fetch_products()
            # update_product_quantity(index, new_quantity)

    async def handle_delete_item(e):
        print("eliminando producto")
        await deleteProductFromCart(token, product["id"])
        await fetch_products()

    return (
        html.tr(
            html.td({"class": "align-middle"},
                    html.div({
                        "style": "display: flex; align-items: center;"},
                        html.img({
                            "src": "static/img/item-1.jpg",
                            "alt": "",
                            "style": "width: 50px;"}),
                        product['name']
                    )
                    ),
            html.td({"class": "align-middle"}, f"${product['price']}"),
            html.td({"class": "align-middle"},
                    html.div({
                        "class": "input-group quantity mx-auto",
                        "style": "width: 100px;"},
                        html.div(
                            {"class": "input-group-btn"},
                            html.button({
                                "class": "btn btn-sm btn-primary btn-minus p-2",
                                "on_click": decrease_quantity  # Manejador de evento para disminuir la cantidad
                            },
                                html.i({
                                    "class": "fa fa-minus"}, "-")
                            )
                        ),
                        html.input({
                            "type": "text",
                            "class": "form-control form-control-sm bg-secondary text-center",
                            "value": quantity,
                            "readonly": ""
                            # Actualizar el estado cuando cambia el input
                        }),
                        html.div(
                            {"class": "input-group-btn"},
                            html.button({
                                "class": "btn btn-sm btn-primary btn-plus p-2",
                                "on_click": increase_quantity  # Manejador de evento para aumentar la cantidad
                            },
                                html.i({
                                    "class": "fa fa-plus"}, "+")
                            )
                        )
                    )
                    ),
            html.td({"class": "align-middle"}, f"${round(product['price'] * quantity, 2)}"),
            html.td({"class": "align-middle"},
                    html.button(
                        {"class": "btn btn-sm btn-primary",
                         "on_click": handle_delete_item},
                        html.i({"class": "fa fa-times"}, "x")
                    )
                    )
        )
    )
