from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from reactpy import component, html
from reactpy_router import route, simple
from reactpy.core.hooks import create_context
from reactpy.backend.fastapi import configure

# componentes
from static.screens.index import App as Index
from static.screens.login import App as Login

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@component
def App():
    context = create_context("value")

    return simple.router(
        route("/", Index(context)),
        route("/login", Login(context)),
        route("/kk", html.h1("kk Page 🏠")),
        route("*", html.h1("Missing Link 🔗‍💥"))
    )


configure(app, App)
