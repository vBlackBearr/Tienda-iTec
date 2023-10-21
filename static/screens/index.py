from fastapi import FastAPI
from reactpy import component, html
from fastapi.staticfiles import StaticFiles
from reactpy.backend.fastapi import configure

# contexto
from reactpy.core.hooks import use_context

# componentes
from static.components.base.banner import banner
from static.components.base.navigationBar import navigationBar
from static.components.base.secondary_nav import secondary_nav
from static.components.base.footer import footer
from static.components.base.main_content import main_content
from static.components.base.css_scripts import css_scripts
from static.components.login import login_form, banner as banner_login

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@component
def App(context):
    value = use_context(context)

    return html.div(
        css_scripts,
        navigationBar,
        banner,
        secondary_nav,
        main_content,


        # Login
        banner_login,
        login_form,


        footer
    )


configure(app, App)
