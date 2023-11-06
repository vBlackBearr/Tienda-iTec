import httpx
from localStoragePy import localStoragePy
from reactpy import use_state, create_context, use_effect


def getSession():
    # User - Tokens
    is_logged_in, set_logged_id = use_state(False)
    user, set_user = use_state({})
    localStorage = localStoragePy('iTec_space', 'your-storage-backend')

    # token = localStorage.getItem(item='token')
    token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImVtYWlsIjoiYWRtaW5AZXhhbXBsZS5jb20iLCJwYXNzd29yZCI6Imhhc2hlZF9wYXNzd29yZF9hZG1pbiJ9LCJleHAiOjE2OTk0NDkxMDN9.IpnZUisiwP2XsczDpX5V-MjjU3XWyINsoEKZt81JBjJX1UqUqlu-fVui_kUzoqIK9j-Dw4cESOc5-tu7InVfV3mjTu7T9wk9OYD5CU82aWonCibVdEwMKX4Ps9hQQo3Dw90MeNZ1WKeSZ3kZqaIt1yXxWfBN7qdNp5cEOevrB6IP0iQTXw9uIKKFWdVZvH0foCaRCqIuZ4pWUj9N8c3xv0x4L5bUIIlFfFhJjso_U4i_0dV8q3bex6gd460G5wWMNYiwZrU1XrDVe6DUkeZb3VN4XHrjmblrCbSdTmdszixHRI4yMSLRIl85Mr-Ibc1jUZC8xcZhY9Lj9PXMzQpQzA"

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
