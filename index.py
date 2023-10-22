from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from reactpy import component, html
from reactpy_router import route, simple
from reactpy.core.hooks import create_context
from reactpy.backend.fastapi import configure

# componentes
from static.screens.index import Index
from static.screens.login import Login
from static.screens.product import Product

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@component
def App():
    context = create_context("value")

    return simple.router(
        route("/", Index(context)),
        route("/login", Login(context)),
        route("/product", Product(context)),
        route("*", html.h1("Missing Link 🔗‍💥"))
    )


configure(app, App)
