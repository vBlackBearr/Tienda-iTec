from reactpy import html
from static.admin.content.base.sidebar import sidebar
from static.admin.content.base.topbar import topbar
from static.admin.content.base.head import head
from static.admin.content.base.footer import footer


def Base(content, context_value):

    return html.main(
        head,
        html.div({
            "id": "wrapper"
        },
            sidebar,
            html.div({
                "id": "content-wrapper",
                "class": "d-flex flex-column"
            },
                html.div({
                    "id": "content"
                },
                    topbar,
                    html.div({
                        "class": "container-fluid"
                    },
                        content
                    )
                ),
                footer
            )
        )


    )
