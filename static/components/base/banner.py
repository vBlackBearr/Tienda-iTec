from reactpy import html

banner = html.div({"class": "banner banner-cover"}, [
    html.div({"class": "banner-container"}, [
        html.h1({"class": "title-cover"}, "iTec"),
        html.a({"class": "btn btn-default"}, "Comprar celulares que te llevan a la perfección")
    ])
])
