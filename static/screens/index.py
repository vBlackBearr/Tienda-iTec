from reactpy import component, html

# contexto
from reactpy.core.hooks import use_context, create_context

# componentes
from static.components.index.banner import banner
from static.components.index.secondary_nav import secondary_nav
from static.components.index.main_content import main_content
from static.screens._base import Base

# LocalStorage
from static.localStorage.localStorage import getSession


@component
def Index(context):
    value = use_context(context)

    # User - Tokens
    session = getSession()
    token = session["token"]

    context = create_context({
        "is_logged_in": session["is_logged_in"],
        "user": session["user"]
    })

    return html.div(
        Base(
            (
                banner,
                secondary_nav,
                main_content
            ),
            context
        )
    )



