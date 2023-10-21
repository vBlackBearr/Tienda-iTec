from reactpy import html

css_scripts = html.div(
    html.link({"rel": "stylesheet", "href": "/static/css/styles.css"}),
    html.link({"rel": "stylesheet", "href": "/static/css/bulma.min.css"}),
    html.link({"rel": "stylesheet", "href": "/static/css/material-design-iconic-font.css"}),
    html.script({"src": "/static/js/main.js"}),
)
