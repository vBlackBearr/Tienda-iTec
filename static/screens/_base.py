from reactpy import component, html

# componentes
from static.components.base.navigationBar import navigationBar
from static.components.base.footer import footer
from static.components.base.css_scripts import css_scripts


@component
def Base(content, context_value):
    return html.div(
        css_scripts,
        navigationBar,

        content,

        footer
    )