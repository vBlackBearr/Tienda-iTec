from reactpy import component, html, use_state

# contexto
from reactpy.core.hooks import use_context

# componentes
from static.screens._base import Base
from static.components.base.banner import banner as banner_login


@component
def Product(context):
    value = use_context(context)
    cantidad, set_cantidad = use_state(1)

    def increaseCantidad(e):
        set_cantidad(cantidad + 1)

    def decreaseCantidad(e):
        if cantidad >= 2:
            set_cantidad(cantidad - 1)

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
                html.div({
                    "class": "product-container row row-cols-1 row-cols-md-5 g-2 g-lg-3 d-flex justify-content-center"},
                    # Carrusel de imágenes
                    html.div({
                        "class": "col-md-4 mb-3",
                    },
                        html.div({
                            "id": "product-carousel",
                            "class": "carousel slide",
                            "data-bs-ride": "carousel"
                        },
                            html.div({
                                "class": "carousel-inner"
                            },
                                html.div({
                                    "class": "carousel-item active"
                                },
                                    html.img({
                                        "src": "static/img/item-1.jpg",
                                        "alt": "Nombre del Producto",
                                        "class": "img-fluid product-image"
                                    })
                                ),
                                html.div({
                                    "class": "carousel-item"
                                },
                                    html.img({
                                        "src": "static/img/item-2.jpg",
                                        "alt": "Nombre del Producto",
                                        "class": "img-fluid product-image"
                                    })
                                ),
                                html.div({
                                    "class": "carousel-item"
                                },
                                    html.img({
                                        "src": "static/img/item-3.jpg",
                                        "alt": "Nombre del Producto",
                                        "class": "img-fluid product-image"
                                    })
                                ),
                                html.div({
                                    "class": "carousel-item"
                                },
                                    html.img({
                                        "src": "static/img/item-4.jpeg",
                                        "alt": "Nombre del Producto",
                                        "class": "img-fluid product-image"
                                    })
                                )
                                # Agrega más imágenes aquí en el mismo formato
                            ),
                            html.a({
                                "class": "carousel-control-prev",
                                "href": "#product-carousel",
                                "role": "button",
                                "data-bs-slide": "prev"
                            },
                                html.span({"class": "carousel-control-prev-icon", "aria-hidden": "true"}),
                                html.span({"class": "visually-hidden"}, "Previous")
                            ),
                            html.a({
                                "class": "carousel-control-next",
                                "href": "#product-carousel",
                                "role": "button",
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
                                                       "name": "size"}),
                                                  html.label({"class": "custom-control-label", "for": "size-1"},
                                                             "128 GB"),
                                              ]),
                                              html.div({"class": "custom-control custom-radio custom-control-inline"}, [
                                                  html.input(
                                                      {"type": "radio", "class": "custom-control-input", "id": "size-2",
                                                       "name": "size"}),
                                                  html.label({"class": "custom-control-label", "for": "size-2"},
                                                             "256 GB"),
                                              ]),
                                              html.div({"class": "custom-control custom-radio custom-control-inline"}, [
                                                  html.input(
                                                      {"type": "radio", "class": "custom-control-input", "id": "size-3",
                                                       "name": "size"}),
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
                                                              "id": "color-1", "name": "color"}),
                                                  html.label({"class": "custom-control-label", "for": "color-1"},
                                                             "Negro"),
                                              ]),
                                              html.div({"class": "custom-control custom-radio custom-control-inline"}, [
                                                  html.input({"type": "radio", "class": "custom-control-input",
                                                              "id": "color-2", "name": "color"}),
                                                  html.label({"class": "custom-control-label", "for": "color-2"},
                                                             "Blanco"),
                                              ]),
                                              html.div({"class": "custom-control custom-radio custom-control-inline"}, [
                                                  html.input({"type": "radio", "class": "custom-control-input",
                                                              "id": "color-3", "name": "color"}),
                                                  html.label({"class": "custom-control-label", "for": "color-3"},
                                                             "Lila"),
                                              ]),
                                              html.div({"class": "custom-control custom-radio custom-control-inline"}, [
                                                  html.input({"type": "radio", "class": "custom-control-input",
                                                              "id": "color-4", "name": "color"}),
                                                  html.label({"class": "custom-control-label", "for": "color-4"},
                                                             "Azul"),
                                              ]),
                                              html.div({"class": "custom-control custom-radio custom-control-inline"}, [
                                                  html.input({"type": "radio", "class": "custom-control-input",
                                                              "id": "color-5", "name": "color"}),
                                                  html.label({"class": "custom-control-label", "for": "color-5"},
                                                             "Rojo"),
                                              ]),
                                              html.div({"class": "custom-control custom-radio custom-control-inline"}, [
                                                  html.input({"type": "radio", "class": "custom-control-input",
                                                              "id": "color-5", "name": "color"}),
                                                  html.label({"class": "custom-control-label", "for": "color-5"},
                                                             "Amarillo Canario"),
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
                                                      "value": cantidad}),
                                          html.div({"class": "input-group-btn"},
                                                   html.button({"class": "btn btn-primary btn-plus",
                                                                "on_click": increaseCantidad},
                                                               html.i({"class": "fa fa-plus"}, "+")
                                                               ),
                                                   ),
                                          ),
                                 html.br(),
                                 # Botón de agregar al carrito
                                 html.button({"class": "btn btn-primary px-3"},
                                             html.i({"class": "fa fa-shopping-cart mr-1"}),
                                             "Add To Cart"
                                             ),
                             ),
                             )
                )
            ),
            value
        )
    )
