from reactpy import html, use_state, web
import reactpy
from static.components.modal import Modal
from static.api import getSession


def LoginForm():

    modal_text, set_modal_text = use_state("")
    modal_style, set_modal_style = use_state({"display": "none"})
    email, set_email = use_state("")
    password, set_password = use_state("")

    @reactpy.event(prevent_default=True)
    async def handleLogin(e):
        # ---activar el modal---
        response = await getSession({"email": email, "password": password})
        if response:
            set_modal_text("Login Success!")
        else:
            set_modal_text("Login Failed!")
        show_modal(None)

    def show_modal(e):
        set_modal_style({"display": "block"})

    def hide_modal(e):
        set_modal_style({"display": "none"})

    return html.div({"class": "container"}, [
        # Modal(login_result="jkljkl", show_modal=show_modal),

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
                html.h2({"class": "is-size-4"}, "Registro"),
                html.form({"action": "#", "class": "form-control"}, [
                    html.input({"type": "email", "placeholder": "Email", "class": "form-control-field"}),
                    html.input({"type": "password", "placeholder": "Password", "class": "form-control-field"}),
                    html.input(
                        {"type": "password", "placeholder": "Confirma tu password", "class": "form-control-field"}),
                    html.button({"class": "btn btn-default btn-primary"}, "Crear cuenta")
                ])
            ])
        ])
    ])
