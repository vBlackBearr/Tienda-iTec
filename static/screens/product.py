from reactpy import component, html

# contexto
from reactpy.core.hooks import use_context

# componentes
from static.screens._base import Base
from static.components.login import banner as banner_login


@component
def Product(context):
    value = use_context(context)
    return html.div(
        Base(
            (
                html.link({
                    "rel": "stylesheet",
                    "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
                }),
                html.script({
                    "src": "static/js/jquery-3.6.0.min.js"
                }),
                html.script({
                    "src": "static/js/bootstrap.min.js"
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
                                        "src": "static/img/item-2.jpg",
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
                             html.h2({"class": "h4 product-name"}, "Nombre del Producto"),
                             # Precio del producto
                             html.p({"class": "text-primary h5 product-price"}, "$19.99"),
                             # Variantes del producto
                             html.select({"class": "form-select product-variants"},
                                         html.option("Variante 1"),
                                         html.option("Variante 2"),
                                         html.option("Variante 3")
                                         ),
                             html.div({
                                 "class": "d-inline p-2"
                             },
                                 # Input numérico para la cantidad
                                 html.div({"class": "input-group mt-3"},
                                          html.span({"class": "input-group-text"}, "Cantidad"),
                                          html.input({"type": "number", "class": "form-control", "value": 1}),
                                          ),
                                 # Botón de agregar al carrito
                                 html.div({"class": "d-flex justify-content-end mt-5"},
                                          html.button({"class": "btn btn-primary add-to-cart-button"},
                                                      "Agregar al Carrito")
                                          )
                             ),
                             )
                )
            ),
            value
        )
    )

