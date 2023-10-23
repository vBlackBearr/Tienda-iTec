from reactpy import html

main_content = (
    html.div(

        # Sección de fotografías
        html.div({"class": "container"}, [
            html.div({"class": "columns is-multiline"}, [
                html.div({"class": "column is-full-mobile"}, [
                    html.div({"class": "columns is-centered is-mobile is-multiline"}, [
                        # 1 Sección de fotografías
                        html.div({"class": "column is-half column-full"}, [
                            html.div({"class": "card"}, [
                                html.span({"class": "price"}, "$18,689"),
                                html.img({"src": "static/img/item-4.jpeg", "alt": ""}),
                                html.div({"class": "card-info"}, [
                                    html.h4({"class": "has-text-black has-text-centered has-text-weight-bold"},
                                            "iPhone 14"),
                                    html.p({"class": "has-text-centered"}, "iPhone con cargador y airpods"),
                                    html.div({"class": "card-buttons"}, [
                                        html.a({"class": "btn btn--mini-rounded", "href": "#"},
                                               html.i({"class": "zmdi zmdi-shopping-cart"})),
                                        html.a({"class": "btn btn--mini-rounded", "href": "#"},
                                               html.i({"class": "zmdi zmdi-favorite-outline"})),
                                        html.a({"class": "btn btn--mini-rounded", "href": "product"},
                                               html.i({"class": "zmdi zmdi-eye"})),
                                    ]),
                                ]),
                            ]),
                        ]),
                        html.div({"class": "column column-full is-half"}, [
                            html.div({"class": "card"}, [
                                html.span({"class": "price"}, "$19,499"),
                                html.img({"src": "static/img/item-3.jpg", "alt": ""}),
                                html.div({"class": "card-info"}, [
                                    html.h4({"class": "has-text-black has-text-centered has-text-weight-bold"},
                                            "iPhone 14 plus"),
                                    html.p({"class": "has-text-centered"}, "iPhone con cargador y airpods"),
                                    html.div({"class": "card-buttons"}, [
                                        html.a({"class": "btn btn--mini-rounded", "href": "#"},
                                               html.i({"class": "zmdi zmdi-shopping-cart"})),
                                        html.a({"class": "btn btn--mini-rounded", "href": "#"},
                                               html.i({"class": "zmdi zmdi-favorite-outline"})),
                                        html.a({"class": "btn btn--mini-rounded", "href": "product"},
                                               html.i({"class": "zmdi zmdi-eye"})),
                                    ]),
                                ]),
                            ]),
                        ]),
                        html.div({"class": "column is-full"}, [
                            html.div({"class": "card"}, [
                                html.span({"class": "price"}, "$21,699"),
                                html.img({"src": "static/img/item-2.jpg", "alt": ""}),
                                html.div({"class": "card-info"}, [
                                    html.h4({"class": "has-text-black has-text-centered has-text-weight-bold"},
                                            "iPhone 14 Pro"),
                                    html.p({"class": "has-text-centered"}, "iPhone con cargador y airpods"),
                                    html.div({"class": "card-buttons"}, [
                                        html.a({"class": "btn btn--mini-rounded", "href": "#"},
                                               html.i({"class": "zmdi zmdi-shopping-cart"})),
                                        html.a({"class": "btn btn--mini-rounded", "href": "#"},
                                               html.i({"class": "zmdi zmdi-favorite-outline"})),
                                        html.a({"class": "btn btn--mini-rounded", "href": "product"},
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
                                html.img({"src": "static/img/item-1.jpg", "alt": ""}),
                                html.div({"class": "card-info"}, [
                                    html.h4({"class": "has-text-black has-text-centered has-text-weight-bold"},
                                            "iPhone 14 Pro Max"),
                                    html.p({"class": "has-text-centered"}, "iPhone con cargador y airpods"),
                                    html.div({"class": "card-buttons"}, [
                                        html.a({"class": "btn btn--mini-rounded", "href": "#"},
                                               html.i({"class": "zmdi zmdi-shopping-cart"})),
                                        html.a({"class": "btn btn--mini-rounded", "href": "#"},
                                               html.i({"class": "zmdi zmdi-favorite-outline"})),
                                        html.a({"class": "btn btn--mini-rounded", "href": "product"},
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
                           # html.p({"class": "has-text-right"}, "Cupon valido en compras menores a 3 dispositvos"),
                            html.div([
                                html.a({"class": "btn btn-default is-size-7", "href": "static/img/lookbook-men.png"}, "Ver cupón"),
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
                          #  html.p({"class": "has-text-right"}, "Valido solo en tienda fisica de la condesa"),
                            html.div([
                                html.a({"class": "btn btn-default is-size-7", "href": "static/img/lookbook-women.png"}, "Ver vale"),
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
                            #html.p({"class": "has-text-right"}, "Valido hasta el 2 de diciembre"),
                            html.div([
                                html.a({"class": "btn btn-default is-size-7", "href": "static/img/lookbook-you.png"}, "Ver cupón"),
                            ]),
                        ]),
                    ]),
                ]),
            ]),
        ]),
    )
)
