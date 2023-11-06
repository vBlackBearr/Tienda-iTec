import httpx
from localStoragePy import localStoragePy
from reactpy import use_state, create_context, use_effect


def getSession():
    # User - Tokens
    is_logged_in, set_logged_id = use_state(False)
    user, set_user = use_state({})
    localStorage = localStoragePy('iTec_space', 'your-storage-backend')

    # token = localStorage.getItem(item='token')
    token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImVtYWlsIjoiYWRtaW5AZXhhbXBsZS5jb20iLCJwYXNzd29yZCI6Imhhc2hlZF9wYXNzd29yZF9hZG1pbiJ9LCJleHAiOjE2OTkyNjc4MDR9.jnfx4FC1xy18HK5fcFzXBtof4tzMgr6EyZzhzcvWcyG5AiEQuzGldX-bVE4YarFrGYWjHnjmaVLHqlZ4i-N197fcr7FiaC2waOFfK1xlDz6qyweBPuCC2N6oweR-MxV1AmVQnhGEGnGrri33-DtZqUMJUZ2eE3ULgz-pQ3bvTaRrVIJ3azS2vcoHKV7zqS-hMqYFM47HDgzAYjUpHcFLY17eRkH3ATUiuLQ_qrBaRJi7COoXIykFeCNt15_AEKdeVfO5bl9xEtUiS09XW2i5n8vAbuLXkJrUpm2WF5gK5hd_mToMTP5fVLPIXtqbdLl8RnnMn3AZQu28FbzlGAtZbQ"

    async def LoadSession():

        if token:
            async with httpx.AsyncClient() as client:
                headers = {"Authorization": token}
                response = await client.post("http://localhost:8000/protected", headers=headers)
            if response.status_code == 200:
                set_user(response.json())
                set_logged_id(True)

    use_effect(LoadSession, [])

    return {"is_logged_in": is_logged_in, "user": user, "token": token}
