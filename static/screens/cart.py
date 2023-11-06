from reactpy import component, html
import asyncio

# contexto
from reactpy.core.hooks import use_context, create_context, use_state, use_effect

from static.components.cart.item import item
# componentes
from static.screens._base import Base
from static.components.base.banner import banner as banner_login
from static.screens.payment import Payment
from reactpy_router import route

# LocalStorage
from static.localStorage.localStorage import getSession

# Api
from static.api import getCart


@component
def Cart(context):
    value = use_context(context)

    # User - Tokens
    session = getSession()
    token = session["token"]

    context = create_context({
        "is_logged_in": session["is_logged_in"],
        "user": session["user"]
    })

    products, set_products = use_state([])
    subtotal, set_subtotal = use_state(0)
    total, set_total = use_state(0)

    async def fetch_products():
        prods = await getCart(token)
        if prods["status"] == 200:
            set_products(prods["data"])
        else:
            print("Error on fetch_products in cart.py: ", prods["status"])
        # set_products(prods)

    use_effect(fetch_products, [])

    def product_rows():
        return [item(product, index) for index, product in enumerate(products)]

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
                html.div({"class": "container-fluid pt-5"},
                         html.div({"class": "row px-xl-5"},
                                  html.div({"class": "col-lg-8 table-responsive mb-5"},
                                           html.table({"class": "table table-bordered text-center mb-0"},
                                                      html.thead({"class": "bg-secondary text-dark"},
                                                                 html.tr(
                                                                     html.th("Productos"),
                                                                     html.th("Precio"),
                                                                     html.th("Cantidad"),
                                                                     html.th("Total"),
                                                                     html.th("Quitar"),
                                                                 )
                                                                 ),
                                                      html.tbody({"class": "align-middle"},

                                                                 *product_rows()
                                                                 # Repite este bloque para cada fila de la tabla
                                                                 )
                                                      )
                                           ),
                                  html.div({"class": "col-lg-4"},
                                           html.form({"class": "mb-5", "action": ""},
                                                     html.div({"class": "input-group"},
                                                              html.input({"type": "text", "class": "form-control p-4",
                                                                          "placeholder": "Coupon Code"}),
                                                              html.div({"class": "input-group-append"},
                                                                       html.button({"class": "btn btn-primary"},
                                                                                   "Aplicar cupón")
                                                                       )
                                                              )
                                                     ),
                                           html.div({"class": "card border-secondary mb-5"},
                                                    html.div({"class": "card-header bg-secondary border-0"},
                                                             html.h4({"class": "font-weight-semi-bold m-0"}, "Cuenta")
                                                             ),
                                                    html.div({"class": "card-body"},
                                                             html.div(
                                                                 {"class": "d-flex justify-content-between mb-3 pt-1"},
                                                                 html.h6({"class": "font-weight-medium"}, "Subtotal"),
                                                                 html.h6({"class": "font-weight-medium"}, "$150")
                                                             ),
                                                             html.div({"class": "d-flex justify-content-between"},
                                                                      html.h6({"class": "font-weight-medium"}, "IVA"),
                                                                      html.h6({"class": "font-weight-medium"}, "$10")
                                                                      )
                                                             ),
                                                    html.div({"class": "card-footer border-secondary bg-transparent"},
                                                             html.div({"class": "d-flex justify-content-between mt-2"},
                                                                      html.h5({"class": "font-weight-bold"}, "Total"),
                                                                      html.h5({"class": "font-weight-bold"}, "$160")
                                                                      ),
                                                             html.a({"class": "btn btn-block btn-primary my-3 py-3",
                                                                     "href": "/payment"}, "Generar compra")
                                                             )
                                                    )
                                           )
                                  )
                         )
            ),
            context
        )
    )
