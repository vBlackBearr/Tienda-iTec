from fastapi import FastAPI
from reactpy import component, html
from fastapi.staticfiles import StaticFiles
from reactpy.backend.fastapi import configure

# contexto
from reactpy.core.hooks import use_context

# componentes
from static.components.base.banner import banner
from static.components.base.secondary_nav import secondary_nav
from static.components.base.main_content import main_content
from static.screens._base import Base

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@component
def App(context):
    value = use_context(context)

    return html.div(

        Base((banner, secondary_nav, main_content), value)

    )


configure(app, App)
