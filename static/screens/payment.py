import aiohttp
from reactpy import component, html
from reactpy_router import route
import httpx
import asyncio
import reactpy
from reactpy import use_context, create_context

from static.api import order
# componentes
from static.screens._base import Base
from static.components.base.banner import banner as banner_login
from reactpy import use_state

# dotenv
from dotenv import load_dotenv

load_dotenv()

# LocalStorage
from static.localStorage.localStorage import getSession


@component
def Payment(context):
    value = use_context(context)

    cantidad, set_cantidad = use_state(1)

    # User - Tokens
    session = getSession()
    token = session["token"]
    is_logged_in = session["is_logged_in"]
    user = session["user"]

    context = create_context({
        "is_logged_in": is_logged_in,
        "user": user
    })

    async def handle_buy(e):
        print("compra")

        data = {
            # "user_id": session["user"]["id"],
            "token": token,
        }

        # getCart

        await order(data)

        # async def getSales():
        #     url = "http://localhost:8000/backend/sales"
        #
        #     async with aiohttp.ClientSession() as session:
        #         async with session.get(url) as response:
        #             if response.status == 200:
        #                 result = await response.json()
        #                 return result
        #             else:
        #                 print(f"Error: {response.status}")

        # async def post():
        #
        # async with aiohttp.ClientSession() as client:
        #
        #     data = {
        #         "user_id": session["user"],
        #         "token": token,
        #     }
        #
        #     response = await client.post("http://localhost:8000/api/order", json=data)
        #
        #     if response.status == 200:
        #         result = response.json()
        #         return result
        #     else:
        #         return None

        # asyncio.ensure_future(post())

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
                                  html.div({"class": "col-lg-8"},
                                           html.div({"class": "mb-4"},
                                                    html.h4({"class": "font-weight-semi-bold mb-4"},
                                                            "Datos del contacto"),
                                                    html.div({"class": "row"},
                                                             html.div({"class": "col-md-6 form-group"},
                                                                      html.label("Nombre"),
                                                                      html.input(
                                                                          {"class": "form-control", "type": "text",
                                                                           "placeholder": "John"}),
                                                                      ),
                                                             html.div({"class": "col-md-6 form-group"},
                                                                      html.label("Apellido Paterno"),
                                                                      html.input(
                                                                          {"class": "form-control", "type": "text",
                                                                           "placeholder": "Doe"}),
                                                                      ),
                                                             html.div({"class": "col-md-6 form-group"},
                                                                      html.label("E-mail"),
                                                                      html.input(
                                                                          {"class": "form-control", "type": "text",
                                                                           "placeholder": "example@email.com"}),
                                                                      ),
                                                             html.div({"class": "col-md-6 form-group"},
                                                                      html.label("Telefono"),
                                                                      html.input(
                                                                          {"class": "form-control", "type": "text",
                                                                           "placeholder": "+123 456 789"}),
                                                                      ),
                                                             html.div({"class": "col-md-6 form-group"},
                                                                      html.label("Direccion 1"),
                                                                      html.input(
                                                                          {"class": "form-control", "type": "text",
                                                                           "placeholder": "123 Street"}),
                                                                      ),
                                                             html.div({"class": "col-md-6 form-group"},
                                                                      html.label("Direccion 2"),
                                                                      html.input(
                                                                          {"class": "form-control", "type": "text",
                                                                           "placeholder": "123 Street"}),
                                                                      ),
                                                             html.div({"class": "col-md-6 form-group"},
                                                                      html.label("Pais"),
                                                                      html.select({"class": "custom-select"},
                                                                                  html.option({"selected": True},
                                                                                              "Selecciona País"),
                                                                                  html.option("México"),
                                                                                  ),
                                                                      ),
                                                             html.div({"class": "col-md-6 form-group"},
                                                                      html.label("Estado"),
                                                                      html.input(
                                                                          {"class": "form-control", "type": "text",
                                                                           "placeholder": "New York"}),
                                                                      ),
                                                             html.div({"class": "col-md-6 form-group"},
                                                                      html.label("Municipio"),
                                                                      html.input(
                                                                          {"class": "form-control", "type": "text",
                                                                           "placeholder": "New York"}),
                                                                      ),
                                                             html.div({"class": "col-md-6 form-group"},
                                                                      html.label("codigo postal"),
                                                                      html.input(
                                                                          {"class": "form-control", "type": "text",
                                                                           "placeholder": "12345"}),
                                                                      ),
                                                             ),
                                                    ),
                                           ),
                                  html.div({"class": "col-lg-4"},
                                           html.div({"class": "card border-secondary mb-5"},
                                                    html.div({"class": "card-header bg-secondary border-0"},
                                                             html.h4({"class": "font-weight-semi-bold m-0"},
                                                                     "Order Total"),
                                                             ),
                                                    html.div({"class": "card-body"},
                                                             html.h5({"class": "font-weight-medium mb-3"}, "Products"),
                                                             html.div({"class": "d-flex justify-content-between"},
                                                                      html.p("iPhone 14 Pro Max"),
                                                                      html.p("$150"),
                                                                      ),
                                                             html.hr({"class": "mt-0"}),
                                                             html.div(
                                                                 {"class": "d-flex justify-content-between mb-3 pt-1"},
                                                                 html.h6({"class": "font-weight-medium"}, "Subtotal"),
                                                                 html.h6({"class": "font-weight-medium"}, "$150"),
                                                             ),
                                                             html.div({"class": "d-flex justify-content-between"},
                                                                      html.h6({"class": "font-weight-medium"}, "IVA"),
                                                                      html.h6({"class": "font-weight-medium"}, "$10"),
                                                                      ),
                                                             ),
                                                    html.div({"class": "card-footer border-secondary bg-transparent"},
                                                             html.div({"class": "d-flex justify-content-between mt-2"},
                                                                      html.h5({"class": "font-weight-bold"}, "Total"),
                                                                      html.h5({"class": "font-weight-bold"}, "$160"),
                                                                      ),
                                                             ),
                                                    ),
                                           html.div({"class": "card border-secondary mb-5"},
                                                    html.div({"class": "card-header bg-secondary border-0"},
                                                             html.h4({"class": "font-weight-semi-bold m-0"}, "Pago"),
                                                             ),
                                                    html.div({"class": "card-body"},
                                                             html.div({"class": "form-group"},
                                                                      html.div({"class": "custom-control custom-radio"},
                                                                               html.input({"type": "radio",
                                                                                           "class": "custom-control-input",
                                                                                           "name": "payment",
                                                                                           "id": "paypal"}),
                                                                               html.label(
                                                                                   {"class": "custom-control-label",
                                                                                    "for": "paypal"}, "Paypal"),
                                                                               ),
                                                                      ),
                                                             html.div({"class": "form-group"},
                                                                      html.div({"class": "custom-control custom-radio"},
                                                                               html.input({"type": "radio",
                                                                                           "class": "custom-control-input",
                                                                                           "name": "payment",
                                                                                           "id": "directcheck"}),
                                                                               html.label(
                                                                                   {"class": "custom-control-label",
                                                                                    "for": "directcheck"},
                                                                                   "Tarjeta de Credito"),
                                                                               ),
                                                                      ),
                                                             html.div({"class": "form-group"},
                                                                      html.div({"class": "custom-control custom-radio"},
                                                                               html.input({"type": "radio",
                                                                                           "class": "custom-control-input",
                                                                                           "name": "payment",
                                                                                           "id": "banktransfer"}),
                                                                               html.label(
                                                                                   {"class": "custom-control-label",
                                                                                    "for": "banktransfer"},
                                                                                   "Tarjeta de Debito"),
                                                                               ),
                                                                      ),
                                                             ),
                                                    # html.div({
                                                    #     "class": "px-5"
                                                    # },
                                                    #     html.input({
                                                    #         "value": cantidad,
                                                    #         "on_change": lambda e: set_cantidad(e["target"]["value"]),
                                                    #         "type": "number",
                                                    #         "class": "form-control"
                                                    #     })
                                                    # ),
                                                    html.div({"class": "card-footer border-secondary bg-transparent"},
                                                             html.button({
                                                                 "class": "btn btn-lg btn-block btn-primary font-weight-bold my-3 py-3",
                                                                 "on_click": handle_buy},
                                                                 "Comprar"),
                                                             ),

                                                    ),
                                           ),
                                  ),
                         )
            ),
            context
        )
    )
