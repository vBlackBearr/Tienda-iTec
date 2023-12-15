from reactpy import html, use_state
import reactpy


def Modal(login_result, show_modal=False):
    modal_style, set_modal_style = use_state({"display": "block" if show_modal else "none"})

    @reactpy.event(prevent_default=True)
    def close_modal(e):
        set_modal_style({"display": "none"})

    return (
        html.div(
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
                            }, login_result),
                            html.button({
                                "type": "button",
                                "class": "btn-close",
                                "data-bs-dismiss": "modal",
                                "aria-label": "Close",
                                "on_click": close_modal
                            })
                        )
                    )
                )
            ),

        )
    )

    # return html.div({"id": "myModal", "class": "modal", "style": modal_style},
    #                 html.div({"class": "modal-content"},
    #                          html.span({"class": "close", "on_click": close_modal}, "×"),
    #                          html.p(None, login_result)
    #                          )
    #                 )
