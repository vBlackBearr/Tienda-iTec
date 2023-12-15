from reactpy import html, use_state, web, use_effect
import reactpy
# from static.components.modal import Modal
from static.api import Login, Register
from localStoragePy import localStoragePy
import httpx

localStorage = localStoragePy('iTec_space', 'your-storage-backend')


def LoginForm():
    modal_text, set_modal_text = use_state("")
    modal_style, set_modal_style = use_state({"display": "none"})
    register_username, set_register_username = use_state("")
    register_email, set_register_email = use_state("")
    register_password, set_register_password = use_state("")
    email, set_email = use_state("")
    password, set_password = use_state("")

    @reactpy.event(prevent_default=True)
    async def handleLogin(e):
        response = await Login({"email": email, "password": password})
        if response["status"] == 200:
            set_modal_text("Login Success!")
            localStorage.setItem('token', response["data"]["token"])
        else:
            if response["status"] == 401:
                set_modal_text("Usuario y/o contraseña incorrecta!")
            else:
                set_modal_text("Error al iniciar sesion")
        show_modal(None)

    @reactpy.event(prevent_default=True)
    async def handleRegister(e):
        response = await Register({"username": register_username,"email": register_email, "password": register_password,
                                   "role_id": 3})
        if response["status"] == 200:
            set_modal_text("Registro Exitoso!")
        else:
            if response["status"] == 401:
                set_modal_text("Usuario y/o contraseña incorrecta!")
            else:
                set_modal_text("Error al Registrar Usuario")
        show_modal(None)

    def show_modal(e):
        set_modal_style({"display": "block"})

    def hide_modal(e):
        set_modal_style({"display": "none"})
        set_modal_text("")

    return html.div({"class": "container"}, [

        #
        #    MODAL
        #
        html.div({
            "style": modal_style,
            "class": "modal"
        },
            html.div({
                "class": "modal-dialog modal-dialog-centered"
            },
                html.div({
                    "class": "modal-content"
                },
                    html.div({
                        "class": "modal-header"
                    },
                        html.h1({
                            "class": "modal-title fs-5",
                            "id": "exampleModalToggleLabel"
                        }, modal_text),
                        html.button({
                            "type": "button",
                            "class": "btn-close",
                            "data-bs-dismiss": "modal",
                            "aria-label": "Close",
                            "on_click": hide_modal
                        })
                    )
                )
            )
        ),
        #
        #   Fin MODAL
        #

        html.div({"class": "columns"}, [
            html.div({"class": "column"}, [
                html.h2({"class": "is-size-4"}, "Iniciar sesión"),
                html.form({"class": "form-control"}, [
                    html.input({
                        "type": "email",
                        "placeholder": "Email",
                        "class": "form-control-field",
                        "on_change": lambda e: set_email(e["target"]["value"]),
                        "value": email
                    }),
                    html.input({
                        "type": "password",
                        "placeholder": "Password",
                        "class": "form-control-field",
                        "on_change": lambda e: set_password(e["target"]["value"]),
                        "value": password
                    }),
                    html.button({
                        "class": "btn btn-default btn-primary",
                        "on_click": handleLogin
                    }, "Iniciar sesión")
                ])
            ]),
            html.div({"class": "column"}, [
                html.h2({
                    "class": "is-size-4"
                }, "Registro"),
                html.form({
                    "action": "#", "class": "form-control"
                }, [
                    html.input({
                        "type": "text", "placeholder": "Username", "class": "form-control-field",
                        "on_change": lambda e: set_register_username(e["target"]["value"])
                    }),
                    html.input({
                        "type": "email", "placeholder": "Email", "class": "form-control-field",
                        "on_change": lambda e: set_register_email(e["target"]["value"])
                    }),
                    html.input({
                        "type": "password", "placeholder": "Password", "class": "form-control-field",
                        "on_change": lambda e: set_register_password(e["target"]["value"])
                    }),
                    html.button({
                        "class": "btn btn-default btn-primary", "on_click": handleRegister
                    }, "Crear cuenta")
                ])
            ])
        ])
    ])
