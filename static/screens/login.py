from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from reactpy import component, html
from reactpy.backend.fastapi import configure

# contexto
from reactpy.core.hooks import use_context

# componentes
from static.components.base.navigationBar import navigationBar
from static.components.login import login_form, banner as banner_login
from static.components.base.footer import footer
from static.components.base.css_scripts import css_scripts

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@component
def App(context):
    value = use_context(context)

    return html.div(
        css_scripts,
        navigationBar,

        # Login
        banner_login,
        login_form,
        html.h1(value),

        footer
    )


configure(app, App)
