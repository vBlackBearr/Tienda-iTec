from localStoragePy import localStoragePy
from reactpy import html
import reactpy


def NavigationBar(is_loged, user):
    # print(user)

    localStorage = localStoragePy('iTec_space', 'your-storage-backend')

    @reactpy.event(prevent_default=True)
    def logout(e):
        print("Logging out")
        localStorage.removeItem('token')

    def ifLogged():
        print(user)
        if user == {}:
            opc = [
                html.li({"class": "nav-menu-item"}, html.a({"class": "nav-menu-link", "href": "login"}, "Registro"))
                ,
                html.li({"class": "nav-menu-item"},
                        html.a({"class": "nav-menu-link", "href": "login"}, "Iniciar Sesión"))
            ]
            return opc
        else:
            return html.li({"class": "nav-menu-item"},
                           html.a({"class": "nav-menu-link", "href": "#", "on_click": logout},
                                  ("Sesion iniciada   Usuario:" + user["email"])))

    return html.header(
        html.nav(
            {"class": "navbar-top"},
            html.ul(
                {"class": "navbar-top-ul"},
                html.li({"class": "navbar-top-item"},
                        html.a({"href": "login", "class": "navbar-top-links"}, "Registro")),
                html.li({"class": "navbar-top-item"},
                        html.a({"href": "login", "class": "navbar-top-links"}, "Iniciar sesión")),
                html.li({"class": "navbar-top-item"}, html.a({"href": "cart", "class": "navbar-top-links"},
                                                             html.i({"class": "zmdi zmdi-shopping-cart"}), " Carrito")
                        )
            )
        ), html.nav({"class": "navbar"}, [
            html.header({"class": "navbar-mobile is-size-5-mobile"}, [
                html.a({"class": "navbar-mobile-link has-text-white", "href": "#", "id": "btn-mobile"}, [
                    html.i({"class": "zmdi zmdi-menu"})
                ]),
                html.a({"class": "navbar-mobile-link has-text-white", "href": "/"}, "iTec"),
                html.a({"class": "navbar-mobile-link has-text-white", "href": "#"}, [
                    html.i({"class": "zmdi zmdi-shopping-cart"}),
                    "Vacio"
                ])
            ]),
            html.nav({"class": "nav-menu", "id": "mySidenav"}, [
                html.form({"class": "form-group", "action": "#"}, [
                    html.div({"class": "form-group-container"}, [
                        html.span({"class": "form-group-icon"}, [
                            html.i({"class": "zmdi zmdi-search"})
                        ]),
                        html.input({"type": "text", "class": "form-group-input", "placeholder": "Buscar..."})
                    ])
                ]),
                html.a({"class": "is-hidden-mobile brand is-uppercase has-text-weight-bold has-text-dark",
                        "href": "/"}, "iTec"),
                html.ul({"class": "nav-menu-ul"}, [
                    html.li({"class": "nav-menu-item", "id": "men"}, [
                        html.a({"class": "nav-menu-link link-submenu active", "href": "#"}, [
                            "Celulares",
                            html.i({"class": "zmdi zmdi-chevron-down"})
                        ]),
                        html.div({"class": "container-sub-menu"}, [
                            html.ul({"class": "sub-menu-ul"}, [
                                html.li({"class": "nav-menu-item"}, [
                                    html.a({"class": "nav-menu-link", "href": "#"}, [
                                        html.strong("iPhone 14"),
                                        html.i({"class": "zmdi zmdi-chevron-down"})
                                    ]),
                                    html.ul({"class": "sub-menu-ul"}, [
                                        html.li({"class": "nav-menu-item"},
                                                html.a({"class": "nav-menu-link", "href": "#"}, "iPhone 14")),
                                        html.li({"class": "nav-menu-item"},
                                                html.a({"class": "nav-menu-link", "href": "#"}, "iPhone 14 plus")),
                                        html.li({"class": "nav-menu-item"},
                                                html.a({"class": "nav-menu-link", "href": "#"}, "iPhone 14 pro")),
                                        html.li({"class": "nav-menu-item"},
                                                html.a({"class": "nav-menu-link", "href": "#"}, "iPhone 14 pro max"))
                                    ])
                                ])
                            ])
                        ])
                    ]),
                    # html.div(ifLogged())
                    html.li({"class": "nav-menu-item", "style": {"display": ["none" if is_loged else "block"]}},
                            html.a({"class": "nav-menu-link", "href": "login"}, "Registro")
                            ),
                    html.li({"class": "nav-menu-item", "style": {"display": ["none" if is_loged else "block"]}},
                            html.a({"class": "nav-menu-link", "href": "login"}, "Iniciar Sesión")),
                    html.li({"class": "nav-menu-item", "style": {"display": ["block" if is_loged else "none"]}},
                            html.a({"class": "nav-menu-link", "href": "#", "on_click": logout},
                                   ("Sesion iniciada   Usuario:" + (user["email"] if is_loged else ""))))
                ])
            ])
        ])
    )
