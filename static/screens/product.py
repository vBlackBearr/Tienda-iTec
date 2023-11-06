from reactpy import component, html, use_state, use_effect
import httpx

# contexto
from reactpy.core.hooks import use_context, create_context

# componentes
from static.screens._base import Base
from static.components.base.banner import banner as banner_login

# api
from static.api import getProducts, patchCartQuantity

# LocalStorage
from static.localStorage.localStorage import getSession


@component
def Product(context):
    value = use_context(context)
    cantidad, set_cantidad = use_state(1)
    color_selected, set_color_selected = use_state("")
    product_id_selected, set_product_id_selected = use_state(0)
    size_selected, set_size_selected = use_state(0)
    products, set_products = use_state([])
    selected_product, set_selected_product = use_state({})

    # Modal
    modal_text, set_modal_text = use_state("")
    modal_style, set_modal_style = use_state({"display": "none"})

    # User - Tokens
    session = getSession()
    token = session["token"]
    is_logged_id = session["is_logged_in"]

    context = create_context({
        "is_logged_in": is_logged_id,
        "user": session["user"]
    })

    def increaseCantidad(e):
        set_cantidad(cantidad + 1)

    def decreaseCantidad(e):
        if cantidad >= 2:
            set_cantidad(cantidad - 1)

    async def fetchProducts():
        prods = await getProducts()
        set_products(prods)
        set_selected_product([
            {
                "src": "static/img/IPHONE14/iphone-14-finish-select-202209-6-1inch.jpeg"
            },
            {
                "src": "static/img/IPHONE14/Azul/iphone-14-finish-select-202209-6-1inch-blue.jpeg"
            },
            {
                "src": "static/img/IPHONE14/Amarillo/iphone-14-finish-select-202209-6-1inch-yellow_AV1.jpeg"
            },
        ])

    use_effect(fetchProducts)

    def color_changed():
        for product in products:
            if product["props"]["color"] == color_selected:
                set_selected_product(product["props"]["images"])

    use_effect(color_changed)

    def create_table_row(product):
        return html.div({
            "class": "carousel-item active"
        },
            html.img({
                "src": product["src"],
                "alt": "Nombre del Producto",
                "class": "img-fluid product-image"
            }),
        )

    async def handle_submit(e):
        if is_logged_id:
            print("agregando al carrito ")
            await patchCartQuantity(token, product_id_selected, cantidad)
            set_modal_text("Producto agregado al carrito")
            show_modal(None)
        else:
            set_modal_text("Primero tienes que iniciar sesion")
            show_modal(None)

    def show_modal(e):
        set_modal_style({"display": "block"})

    def hide_modal(e):
        set_modal_style({"display": "none"})
        set_modal_text("")


    return html.div(
        Base(
            (
                html.link({
                    "rel": "stylesheet",
                    "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
                }),
                html.link({
                    "rel": "stylesheet",
                    "href": "/static/css/material-design-iconic-font.css"
                }),
                html.link({
                    "rel": "stylesheet",
                    "href": "/static/css/style.min.css"
                }),
                html.link({
                    "rel": "stylesheet",
                    "href": "/static/css/style.css"
                }),
                html.link({
                    "rel": "stylesheet",
                    "href": "/static/css/styles.css"
                }),
                html.script({
                    "src": "static/js/jquery-3.6.0.min.js"
                }),
                html.script({
                    "src": "static/js/bootstrap.min.js"
                }),
                html.script({
                    "src": "static/js/main.js"
                }),
                banner_login,
                # Contenedor principal de información del producto
                #
                #    MODAL
                #
                html.div({
                    "style": modal_style,
                    "class": "modal"
                },
                    html.div({
                        "class": "modal-dialog modal-dialog-centered"
                    },
                        html.div({
                            "class": "modal-content"
                        },
                            html.div({
                                "class": "modal-header"
                            },
                                html.h1({
                                    "class": "modal-title fs-5",
                                    "id": "exampleModalToggleLabel"
                                }, modal_text),
                                html.button({
                                    "type": "button",
                                    "class": "btn-close",
                                    "data-bs-dismiss": "modal",
                                    "aria-label": "Close",
                                    "on_click": hide_modal
                                })
                            )
                        )
                    )
                ),
                #
                #   Fin MODAL
                #
                html.div({
                    "class": "product-container row row-cols-1 row-cols-md-10 g-2 g-lg-3 d-flex justify-content-center",
                    "style": {
                        "background-color": "#f5f5f7",
                        "padding-bottom": "30px",
                        "padding-top": "30px"
                    }},
                    # Carrusel de imágenes
                    html.div({
                        "class": "col-md-6 mb-3",
                    },
                        html.div({
                            "id": "carouselExample",
                            "class": "carousel carousel-dark carousel-fade",
                            "data-bs-ride": "carousel"
                        },
                            html.div({
                                "class": "carousel-inner"
                            },
                                [create_table_row(row) for row in selected_product],
                            ),
                            html.button(
                                {
                                    "class": "carousel-control-prev",
                                    "type": "button",
                                    "data-bs-target": "#carouselExample",
                                    "data-bs-slide": "prev"
                                },
                                html.span({"class": "carousel-control-prev-icon", "aria-hidden": "true"}),
                                html.span({"class": "visually-hidden"}, "Previous")
                            ),
                            html.button(
                                {
                                    "class": "carousel-control-next",
                                    "type": "button",
                                    "data-bs-target": "#carouselExample",
                                    "data-bs-slide": "next"
                                },
                                html.span({"class": "carousel-control-next-icon", "aria-hidden": "true"}),
                                html.span({"class": "visually-hidden"}, "Next")
                            )
                        )
                    ),
                    # Contenedor de detalles del producto
                    html.div({"class": "col-md-6 ps-5"},
                             # Nombre del producto
                             html.h2({"class": "h4 product-name"}, "iPhone 14"),
                             # Precio del producto
                             html.p({"class": "text-primary h5 product-price"}, "$949.99"),
                             html.div({
                                 "class": "d-inline p-2"
                             },
                                 # Tamaños
                                 html.div({"class": "d-flex mb-3"},
                                          html.p({"class": "text-dark font-weight-medium mb-0 mr-3"}, "Memoria:"),
                                          html.form([
                                              html.div({"class": "custom-control custom-radio custom-control-inline"}, [
                                                  html.input(
                                                      {"type": "radio", "class": "custom-control-input", "id": "size-1",
                                                       "name": "size",
                                                       "on_change": lambda e: set_size_selected(128)}),
                                                  html.label({"class": "custom-control-label", "for": "size-1"},
                                                             "128 GB"),
                                              ]),
                                              html.div({"class": "custom-control custom-radio custom-control-inline"}, [
                                                  html.input(
                                                      {"type": "radio", "class": "custom-control-input", "id": "size-2",
                                                       "name": "size",
                                                       "on_change": lambda e: set_size_selected(256)}),
                                                  html.label({"class": "custom-control-label", "for": "size-2"},
                                                             "256 GB"),
                                              ]),
                                              html.div({"class": "custom-control custom-radio custom-control-inline"}, [
                                                  html.input(
                                                      {"type": "radio", "class": "custom-control-input", "id": "size-3",
                                                       "name": "size",
                                                       "on_change": lambda e: set_size_selected(512)}),
                                                  html.label({"class": "custom-control-label", "for": "size-3"},
                                                             "512 GB"),
                                              ]),
                                          ]),
                                          ),
                                 # Colores
                                 html.div({"class": "d-flex mb-4"},
                                          html.p({"class": "text-dark font-weight-medium mb-0 mr-3"}, "Colors:"),
                                          html.form([
                                              html.div({"class": "custom-control custom-radio custom-control-inline"}, [
                                                  html.input({"type": "radio", "class": "custom-control-input",
                                                              "id": "color-1", "name": "color",
                                                              "value": "Azul",
                                                              "on_change": lambda e: [set_color_selected("Azul"),
                                                                                      set_product_id_selected(17)]}),
                                                  html.label({"class": "custom-control-label", "for": "color-1"},
                                                             "Azul"),
                                              ]),
                                              html.div({"class": "custom-control custom-radio custom-control-inline"}, [
                                                  html.input({"type": "radio", "class": "custom-control-input",
                                                              "id": "color-2", "name": "color",
                                                              "value": "Morado",
                                                              "on_change": lambda e: [set_color_selected("Morado"),
                                                                                      set_product_id_selected(18)]}),
                                                  html.label({"class": "custom-control-label", "for": "color-2"},
                                                             "Morado"),
                                              ]),
                                              html.div({"class": "custom-control custom-radio custom-control-inline"}, [
                                                  html.input({"type": "radio", "class": "custom-control-input",
                                                              "id": "color-3", "name": "color",
                                                              "value": "Amarillo",
                                                              "on_change": lambda e: [set_color_selected("Amarillo"),
                                                                                      set_product_id_selected(19)]}),
                                                  html.label({"class": "custom-control-label", "for": "color-3"},
                                                             "Amarillo"),
                                              ]),
                                              html.div({"class": "custom-control custom-radio custom-control-inline"}, [
                                                  html.input({"type": "radio", "class": "custom-control-input",
                                                              "id": "color-4", "name": "color",
                                                              "value": "Medianoche",
                                                              "on_change": lambda e: [set_color_selected("Medianoche"),
                                                                                      set_product_id_selected(209)]}),
                                                  html.label({"class": "custom-control-label", "for": "color-4"},
                                                             "Medianoche"),
                                              ]),
                                              html.div({"class": "custom-control custom-radio custom-control-inline"}, [
                                                  html.input({"type": "radio", "class": "custom-control-input",
                                                              "id": "color-5", "name": "color",
                                                              "value": "Blanco estelar",
                                                              "on_change": lambda e: [set_color_selected(
                                                                  "Blanco estelar"), set_product_id_selected(21)]}),
                                                  html.label({"class": "custom-control-label", "for": "color-5"},
                                                             "Blanco estelar"),
                                              ]),
                                              html.div({"class": "custom-control custom-radio custom-control-inline"}, [
                                                  html.input({"type": "radio", "class": "custom-control-input",
                                                              "id": "color-6", "name": "color",
                                                              "value": "RED",
                                                              "on_change": lambda e: [set_color_selected("RED"),
                                                                                      set_product_id_selected(22)]}),
                                                  html.label({"class": "custom-control-label", "for": "color-6"},
                                                             "RED"),
                                              ]),
                                          ]),
                                          ),
                                 # Input numérico para la cantidad
                                 html.div({"class": "input-group quantity mr-3", "style": "width: 130px;"},
                                          html.div({"class": "input-group-btn"},
                                                   html.button({"class": "btn btn-primary btn-minus",
                                                                "on_click": decreaseCantidad},
                                                               html.i({"class": "fa fa-minus"}, "-")
                                                               ),
                                                   ),
                                          html.input({"type": "text", "class": "form-control bg-secondary text-center",
                                                      "value": cantidad,
                                                      "readonly": ""}),
                                          html.div({"class": "input-group-btn"},
                                                   html.button({"class": "btn btn-primary btn-plus",
                                                                "on_click": increaseCantidad},
                                                               html.i({"class": "fa fa-plus"}, "+")
                                                               ),
                                                   ),
                                          ),
                                 html.br(),
                                 # Botón de agregar al carrito
                                 html.button({
                                     "class": "btn btn-primary px-3",
                                     "on_click": handle_submit
                                 },
                                     html.i({"class": "fa fa-shopping-cart mr-1"}),
                                     "Add To Cart"
                                 ),
                             ),
                             )
                )
            ),
            context
        )
    )
