from reactpy import component, html

# contexto
from reactpy.core.hooks import use_context

# componentes
from static.components.login import LoginForm
from static.components.base.banner import banner
from static.screens._base import Base


@component
def Login(context):
    context_value = use_context(context)

    content = (
        banner,
        html.link({
            "rel": "stylesheet",
            "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
        }),
        html.script({"src": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"}),
        LoginForm()
    )

    return html.div(

        # Login
        Base(
            content,
            context_value
        ),

        # html.h1(value),
    )

