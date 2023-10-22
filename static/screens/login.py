from reactpy import component, html

# contexto
from reactpy.core.hooks import use_context

# componentes
from static.components.login import login_form, banner as banner_login
from static.screens._base import Base


@component
def Login(context):
    context_value = use_context(context)

    content = (
        banner_login,
        login_form
    )

    return html.div(

        # Login
        Base(
            content,
            context_value
        ),

        # html.h1(value),
    )

