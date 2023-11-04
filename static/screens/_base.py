import httpx
from reactpy import component, html, use_state, use_effect
from localStoragePy import localStoragePy

from static.api import Login
# componentes
from static.components.base.navigationBar import NavigationBar
from static.components.base.footer import footer
from static.components.base.css_scripts import css_scripts


@component
def Base(content, context_value):
    is_logged_in, set_logged_id = use_state(False)
    user, set_user = use_state({})

    localStorage = localStoragePy('iTec_space', 'your-storage-backend')

    async def LoadSession():

        token = localStorage.getItem(item='token')
        if token:
            async with httpx.AsyncClient() as client:
                headers = {"Authorization": token}
                response = await client.post("http://localhost:8000/protected", headers=headers)
            if response.status_code == 200:
                set_user(response.json())
                set_logged_id(True)

    use_effect(LoadSession, [])

    return html.div(
        css_scripts,
        NavigationBar(is_logged_in, user),

        content,

        footer
    )
