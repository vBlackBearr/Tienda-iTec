from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from reactpy import component, html
from reactpy.backend.fastapi import configure

# contexto
from reactpy.core.hooks import use_context

# componentes
from static.components.login import login_form, banner as banner_login

from static.screens._base import Base

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@component
def App(context):
    value = use_context(context)

    content = (banner_login, login_form)

    return html.div(

        # Login
        Base(content,value),

        # html.h1(value),
    )


configure(app, App)
