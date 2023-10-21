from fastapi import FastAPI
from reactpy import component, html
from fastapi.staticfiles import StaticFiles
from reactpy.backend.fastapi import configure

# componentes
from static.components.base.navigationBar import navigationBar
from static.components.base.footer import footer
from static.components.base.css_scripts import css_scripts

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@component
def Base(content, context_value):

    return html.div(
        css_scripts,
        navigationBar,

        content,

        footer
    )


configure(app, Base)
