from reactpy import component, html

# contexto
from reactpy.core.hooks import use_context, create_context

# componentes
from static.screens._base import Base
from static.components.base.banner import banner as banner_login
from static.screens.payment import Payment
from reactpy_router import route

# LocalStorage
from static.localStorage.localStorage import getSession


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
                                                                 html.tr(
                                                                     html.td({"class": "align-middle"},
                                                                             html.div({
                                                                                          "style": "display: flex; align-items: center;"},
                                                                                      html.img({
                                                                                                   "src": "static/img/item-1.jpg",
                                                                                                   "alt": "",
                                                                                                   "style": "width: 50px;"}),
                                                                                      "iPhone 14 pro Max"
                                                                                      )
                                                                             ),
                                                                     html.td({"class": "align-middle"}, "$150"),
                                                                     html.td({"class": "align-middle"},
                                                                             html.div({
                                                                                          "class": "input-group quantity mx-auto",
                                                                                          "style": "width: 100px;"},
                                                                                      html.div(
                                                                                          {"class": "input-group-btn"},
                                                                                          html.button({
                                                                                                          "class": "btn btn-sm btn-primary btn-minus"},
                                                                                                      html.i({
                                                                                                                 "class": "fa fa-minus"})
                                                                                                      )
                                                                                          ),
                                                                                      html.input({"type": "text",
                                                                                                  "class": "form-control form-control-sm bg-secondary text-center",
                                                                                                  "value": "1"}),
                                                                                      html.div(
                                                                                          {"class": "input-group-btn"},
                                                                                          html.button({
                                                                                                          "class": "btn btn-sm btn-primary btn-plus"},
                                                                                                      html.i({
                                                                                                                 "class": "fa fa-plus"})
                                                                                                      )
                                                                                          )
                                                                                      )
                                                                             ),
                                                                     html.td({"class": "align-middle"}, "$150"),
                                                                     html.td({"class": "align-middle"},
                                                                             html.button(
                                                                                 {"class": "btn btn-sm btn-primary"},
                                                                                 html.i({"class": "fa fa-times"})
                                                                                 )
                                                                             )
                                                                 ),
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
