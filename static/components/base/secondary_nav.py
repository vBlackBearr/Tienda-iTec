from reactpy import html

secondary_nav = html.div({"class": "container"}, [
    html.nav({"class": "nav"}, [
        html.a({"class": "nav-item active has-text-weight-semibold", "href": "#"}, "Popular"),
        html.a({"class": "nav-item has-text-weight-semibold", "href": "#"}, "Novedades"),
        html.a({"class": "nav-item has-text-weight-semibold", "href": "#"}, "Más vendidos"),
        html.a({"class": "nav-item has-text-weight-semibold", "href": "#"}, "Ofertas")
    ])
])
