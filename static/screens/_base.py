import httpx
from reactpy import component, html, use_state, use_effect, use_context

from static.api import Login
# componentes
from static.components.base.navigationBar import NavigationBar
from static.components.base.footer import footer
from static.components.base.css_scripts import css_scripts


@component
def Base(content, context):

    context2 = use_context(context)

    return html.div(
        css_scripts,
        NavigationBar(context2["is_logged_in"], context2["user"]),

        content,

        footer
    )
