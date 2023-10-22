from reactpy import component, html

# contexto
from reactpy.core.hooks import use_context

# componentes
from static.components.index.banner import banner
from static.components.index.secondary_nav import secondary_nav
from static.components.index.main_content import main_content
from static.screens._base import Base


@component
def Index(context):
    value = use_context(context)

    return html.div(
        Base(
            (
                banner,
                secondary_nav,
                main_content
            ),
            value
        )
    )



