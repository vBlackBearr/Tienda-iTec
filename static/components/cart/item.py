from reactpy import use_state, html, component


@component
def item(product, index):
    quantity, set_quantity = use_state(product['quantity'])

    def increase_quantity(e):
        new_quantity = quantity + 1
        set_quantity(new_quantity)
        # update_product_quantity(index, new_quantity)

    def decrease_quantity(e):
        if quantity >= 2:
            new_quantity = quantity - 1
            set_quantity(new_quantity)
            # update_product_quantity(index, new_quantity)

    # def update_product_quantity(index, new_quantity):
    #     products_copy = products.copy()
    #     products_copy[index]['quantity'] = new_quantity
    #     set_products(products_copy)

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
                            "on_change": lambda e: set_quantity(int(e.target.value))
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
            html.td({"class": "align-middle"}, f"${product['price']}"),
            html.td({"class": "align-middle"},
                    html.button(
                        {"class": "btn btn-sm btn-primary"},
                        html.i({"class": "fa fa-times"})
                    )
                    )
        )
    )
