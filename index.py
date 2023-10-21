from fastapi import FastAPI
from reactpy import component, html
from fastapi.staticfiles import StaticFiles
from reactpy.backend.fastapi import configure

# componentes
from static.components.base.banner import banner
from static.components.base.navigationBar import navigationBar
from static.components.base.secondary_nav import secondary_nav
from static.components.base.footer import footer
from static.components.base.main_content import main_content

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
        banner,
        secondary_nav,
        main_content,
        footer
    )


configure(app, App)
