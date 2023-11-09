from reactpy import html

footer = html.footer({"class": "footer"}, [
    html.div({"class": "container"}, [
        html.div({"class": "columns is-multiline"}, [
            html.div({"class": "column"}, [
                html.ul({"class": "footer-ul"}, [
                    html.li({"class": "footer-item"}, [
                        html.h3({"class": "has-text-weight-bold"}, "Porqué comprar")
                    ]),
                    html.li({"class": "footer-item"}, "Envios y retornos"),
                    html.li({"class": "footer-item"}, "Envios seguros"),
                    html.li({"class": "footer-item"}, "Etival trading")
                ])
            ]),
            html.div({"class": "column"}, [
                html.ul({"class": "footer-ul"}, [
                    html.li({"class": "footer-item"}, [
                        html.h3({"class": "has-text-weight-bold"}, "Tu cuenta")
                    ]),
                    html.li({"class": "footer-item"}, html.a({"class": "footer-link", "href": "/login"}, "Iniciar sesión")),
                    html.li({"class": "footer-item"}, html.a({"class": "footer-link", "href": "/login"}, "Registro")),
                    html.li({"class": "footer-item"}, html.a({"class": "footer-link", "href": "/cart"}, "Ver carrito")),
                    html.li({"class": "footer-item"}, html.a({"class": "footer-link", "href": "/product"}, "Ver catálogo"))
                ])
            ]),
            html.div({"class": "column"}, [
                html.ul({"class": "footer-ul"}, [
                    html.li({"class": "footer-item"}, [
                        html.h3({"class": "has-text-weight-bold"}, "Catalogo")
                    ]),
                    html.li({"class": "footer-item"}, html.a({"class": "footer-link"}, "Ver tu Catalogo")),
                    html.li({"class": "footer-item"}, html.a({"class": "footer-link"}, "Privacidad y cookies")),
                    html.li({"class": "footer-item"}, html.a({"class": "footer-link"}, "Borrar tu catalogo"))
                ])
            ]),
            html.div({"class": "column is-full"}, [
                html.div({"class": "footer-socials"}, [
                    html.a({"class": "footer-solcials-link", "href": "#"}, html.i({"class": "zmdi zmdi-facebook"})),
                    html.a({"class": "footer-solcials-link", "href": "#"}, html.i({"class": "zmdi zmdi-twitter"})),
                    html.a({"class": "footer-solcials-link", "href": "#"}, html.i({"class": "zmdi zmdi-instagram"})),
                    html.a({"class": "footer-solcials-link", "href": "#"}, html.i({"class": "zmdi zmdi-pinterest"}))
                ])
            ])
        ])
    ]),
    html.div({"class": "footer-bar-top"}, [
        html.div({"class": "container"}, [
            html.a({"class": "footer-bar-top-links", "href": "#"}, "2019 Avenue Fashion")
        ])
    ])
])
