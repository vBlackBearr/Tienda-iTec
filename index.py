from fastapi import FastAPI
from reactpy import component, html, use_state, use_effect
from fastapi.staticfiles import StaticFiles
from reactpy.backend.fastapi import configure

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@component
def NavigationBar():
    return html.nav(
        {"class": "navbar-top"},
        html.ul(
            {"class": "navbar-top-ul"},
            html.li({"class": "navbar-top-item"},
                    html.a({"href": "registro.html", "class": "navbar-top-links"}, "Registro")),
            html.li({"class": "navbar-top-item"},
                    html.a({"href": "login.html", "class": "navbar-top-links"}, "Iniciar sesión")),
            html.li({"class": "navbar-top-item"}, html.a({"href": "#", "class": "navbar-top-links"},
                                                         html.i({"class": "zmdi zmdi-shopping-cart"}), " Carrito")
                    )
        )
    )


@component
def Header():
    return html.header(
        html.div({"class": "container"},
                 html.a({"href": "/index"}, html.h1({"class": "title-cover"}, "iTec")),
                 html.button({"class": "btn btn-default"}, "Comprar celulares que te llevan a la perfección")
                 )
    )


@component
def MainContent():
    return html.div(
        # Barra de navegación secundaria
        html.div({"class": "container"}, [
            html.nav({"class": "nav"}, [
                html.a({"class": "nav-item active has-text-weight-semibold", "href": "#"}, "Popular"),
                html.a({"class": "nav-item has-text-weight-semibold", "href": "#"}, "Novedades"),
                html.a({"class": "nav-item has-text-weight-semibold", "href": "#"}, "Más vendidos"),
                html.a({"class": "nav-item has-text-weight-semibold", "href": "#"}, "Ofertas"),
            ]),
        ]),

        # Sección de fotografías
        html.div({"class": "container"}, [
            html.div({"class": "columns is-multiline"}, [
                html.div({"class": "column is-full-mobile"}, [
                    html.div({"class": "columns is-centered is-mobile is-multiline"}, [
                        # 1 Sección de fotografías
                        html.div({"class": "column is-half column-full"}, [
                            html.div({"class": "card"}, [
                                html.span({"class": "price"}, "$18,689"),
                                html.img({"src": "static/img/item-1.png", "alt": ""}),
                                html.div({"class": "card-info"}, [
                                    html.h4({"class": "has-text-black has-text-centered has-text-weight-bold"},
                                            "iPhone 14"),
                                    html.p({"class": "has-text-centered"}, "iPhone con cargador y airpods"),
                                    html.div({"class": "card-buttons"}, [
                                        html.a({"class": "btn btn--mini-rounded", "href": "#"},
                                               html.i({"class": "zmdi zmdi-shopping-cart"})),
                                        html.a({"class": "btn btn--mini-rounded", "href": "#"},
                                               html.i({"class": "zmdi zmdi-favorite-outline"})),
                                        html.a({"class": "btn btn--mini-rounded", "href": "producto.html"},
                                               html.i({"class": "zmdi zmdi-eye"})),
                                    ]),
                                ]),
                            ]),
                        ]),
                        html.div({"class": "column column-full is-half"}, [
                            html.div({"class": "card"}, [
                                html.span({"class": "price"}, "$19,499"),
                                html.img({"src": "static/img/item-2.png", "alt": ""}),
                                html.div({"class": "card-info"}, [
                                    html.h4({"class": "has-text-black has-text-centered has-text-weight-bold"},
                                            "iPhone 14 plus"),
                                    html.p({"class": "has-text-centered"}, "iPhone con cargador y airpods"),
                                    html.div({"class": "card-buttons"}, [
                                        html.a({"class": "btn btn--mini-rounded", "href": "#"},
                                               html.i({"class": "zmdi zmdi-shopping-cart"})),
                                        html.a({"class": "btn btn--mini-rounded", "href": "#"},
                                               html.i({"class": "zmdi zmdi-favorite-outline"})),
                                        html.a({"class": "btn btn--mini-rounded", "href": "producto.html"},
                                               html.i({"class": "zmdi zmdi-eye"})),
                                    ]),
                                ]),
                            ]),
                        ]),
                        html.div({"class": "column is-full"}, [
                            html.div({"class": "card"}, [
                                html.span({"class": "price"}, "$21,699"),
                                html.img({"src": "static/img/item-3.png", "alt": ""}),
                                html.div({"class": "card-info"}, [
                                    html.h4({"class": "has-text-black has-text-centered has-text-weight-bold"},
                                            "iPhone 14 Pro"),
                                    html.p({"class": "has-text-centered"}, "iPhone con cargador y airpods"),
                                    html.div({"class": "card-buttons"}, [
                                        html.a({"class": "btn btn--mini-rounded", "href": "#"},
                                               html.i({"class": "zmdi zmdi-shopping-cart"})),
                                        html.a({"class": "btn btn--mini-rounded", "href": "#"},
                                               html.i({"class": "zmdi zmdi-favorite-outline"})),
                                        html.a({"class": "btn btn--mini-rounded", "href": "producto.html"},
                                               html.i({"class": "zmdi zmdi-eye"})),
                                    ]),
                                ]),
                            ]),
                        ]),
                    ]),
                ]),
                # Segunda sección de fotografías
                html.div({"class": "column is-half is-full-mobile"}, [
                    html.div({"class": "columns is-mobile is-multiline"}, [
                        html.div({"class": "column is-full"}, [
                            html.div({"class": "card"}, [
                                html.span({"class": "price"}, "$23,469"),
                                html.img({"src": "static/img/item-4.png", "alt": ""}),
                                html.div({"class": "card-info"}, [
                                    html.h4({"class": "has-text-black has-text-centered has-text-weight-bold"},
                                            "iPhone 14 Pro Max"),
                                    html.p({"class": "has-text-centered"}, "iPhone con cargador y airpods"),
                                    html.div({"class": "card-buttons"}, [
                                        html.a({"class": "btn btn--mini-rounded", "href": "#"},
                                               html.i({"class": "zmdi zmdi-shopping-cart"})),
                                        html.a({"class": "btn btn--mini-rounded", "href": "#"},
                                               html.i({"class": "zmdi zmdi-favorite-outline"})),
                                        html.a({"class": "btn btn--mini-rounded", "href": "producto.html"},
                                               html.i({"class": "zmdi zmdi-eye"})),
                                    ]),
                                ]),
                            ]),
                        ]),
                    ]),
                ]),
            ]),
        ]),
        # Tercera sección
        html.div({"class": "container container-full"}, [
            html.div({"class": "columns is-centered is-multiline"}, [
                html.div({"class": "column is-full"}, [
                    html.div({"class": "separator"}),
                ]),
                html.div({"class": "column is-half-tablet is-one-third-desktop column-half"}, [
                    html.div({"class": "card card-second"}, [
                        html.img({"class": "card-second-image", "src": "static/img/lookbook-men.png", "alt": ""}),
                        html.div({"class": "card-second-body --text-right"}, [
                            html.h1({"class": "has-text-right is-size-4 has-text-weight-semibold-bold"},
                                    "Cupones 5% de descuento"),
                            html.p({"class": "has-text-right"}, "Cupon valido en compras menores a 3 dispositovs"),
                            html.div([
                                html.a({"class": "btn btn-default is-size-7", "href": "#"}, "Canjear"),
                            ]),
                        ]),
                    ]),
                ]),
                html.div({"class": "column is-half-tablet is-one-third-desktop column-half"}, [
                    html.div({"class": "card card-second"}, [
                        html.img({"class": "card-second-image", "src": "static/img/lookbook-women.png", "alt": ""}),
                        html.div({"class": "card-second-body --text-right"}, [
                            html.h1({"class": "has-text-right is-size-4 has-text-weight-semibold-bold"},
                                    "Descuento del 25%"),
                            html.p({"class": "has-text-right"}, "Valido solo en tienda fisica de la condesa"),
                            html.div([
                                html.a({"class": "btn btn-default is-size-7", "href": "#"}, "Ver vale"),
                            ]),
                        ]),
                    ]),
                ]),
                html.div({"class": "column is-half-tablet is-one-third-desktop"}, [
                    html.div({"class": "card card-second"}, [
                        html.img({"class": "card-second-image", "src": "static/img/lookbook-you.png", "alt": ""}),
                        html.div({"class": "card-second-body --text-right"}, [
                            html.h1({"class": "has-text-right is-size-4 has-text-weight-semibold-bold"},
                                    "Vale del 10% en todos los dispositivos"),
                            html.p({"class": "has-text-right"}, "Valido hasta el 2 de diciembre"),
                            html.div([
                                html.a({"class": "btn btn-default is-size-7", "href": "#"}, "Canjear"),
                            ]),
                        ]),
                    ]),
                ]),
            ]),
        ]),
    )


@component
def Footer():
    return html.footer(
        {"class": "footer"},
        html.div({"class": "container"},
                 # Agrega aquí el contenido del pie de página
                 ),
        html.div({"class": "footer-bar-top"},
                 html.a({"class": "footer-bar-top-links", "href": "#"}, "2019 Avenue Fashion")
                 )
    )


@component
def App():
    return html.div(
        html.link({"rel": "stylesheet", "href": "/static/css/styles.css"}),
        html.link({"rel": "stylesheet", "href": "/static/css/bulma.min.css"}),
        html.link({"rel": "stylesheet", "href": "/static/css/material-design-icons-font.css"}),
        html.script({"src": "/static/js/main.js"}),
        NavigationBar(),
        Header(),
        MainContent(),
        Footer()
    )


configure(app, App)
