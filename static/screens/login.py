from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from reactpy import component, html
from reactpy.backend.fastapi import configure

from static.components.base.footer import footer
# componentes
from static.components.base.navigationBar import navigationBar
from static.components.login import login_form, banner as banner_login

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@component
def App():
    return html.div(
        html.link({"rel": "stylesheet", "href": "/static/css/styles.css"}),
        html.link({"rel": "stylesheet", "href": "/static/css/bulma.min.css"}),
        html.link({"rel": "stylesheet", "href": "/static/css/material-design-icons-font.css"}),
        html.script({"src": "/static/js/main.js"}),
        navigationBar,

        # Login
        banner_login,
        login_form,

        footer
    )


configure(app, App)
