from reactpy import html

banner = html.div({"class": "banner banner-second"}, [
    html.div({"class": "banner-container"}, [
        html.h1("iTec"),
        html.h2("Think Different")
    ])
])

login_form = html.div({"class": "container"}, [
    html.div({"class": "columns"}, [
        html.div({"class": "column"}, [
            html.h2({"class": "is-size-4"}, "Iniciar sesión"),
            html.form({"action": "#", "class": "form-control"}, [
                html.input({"type": "email", "placeholder": "Email", "class": "form-control-field error"}),
                html.input({"type": "password", "placeholder": "Password", "class": "form-control-field"}),
                html.button({"class": "btn btn-default btn-primary"}, "Iniciar sesión")
            ])
        ]),
        html.div({"class": "column"}, [
            html.h2({"class": "is-size-4"}, "Registro"),
            html.form({"action": "#", "class": "form-control"}, [
                html.input({"type": "email", "placeholder": "Email", "class": "form-control-field"}),
                html.input({"type": "password", "placeholder": "Password", "class": "form-control-field"}),
                html.input({"type": "password", "placeholder": "Confirma tu password", "class": "form-control-field"}),
                html.button({"class": "btn btn-default btn-primary"}, "Crear cuenta")
            ])
        ])
    ])
])
