from reactpy import html

footer = html.footer(
        {"class": "footer"},
        html.div({"class": "container"},
                 # Agrega aquí el contenido del pie de página
                 ),
        html.div({"class": "footer-bar-top"},
                 html.a({"class": "footer-bar-top-links", "href": "#"}, "2019 Avenue Fashion")
                 )
    )