from reactpy import html, use_state
import reactpy


def login():

    email, set_email = use_state("")
    password1, set_password = use_state("")

    @reactpy.event(prevent_default=True)
    async def handleLogin(e):
        response = await Login({"email": email, "password": password})
        if response["status"] == 200:
            set_modal_text("Login Success!")
            localStorage.setItem('token', response["data"]["token"])
        else:
            if response["status"] == 401:
                set_modal_text("Usuario y/o contraseña incorrecta!")
            else:
                set_modal_text("Error al iniciar sesion")
        show_modal(None)

    return (
        html.div({"class": "container"},
                 html.div({"class": "row justify-content-center"},
                          html.div({"class": "col-xl-10 col-lg-12 col-md-9"},
                                   html.div({"class": "card o-hidden border-0 shadow-lg my-5"},
                                            html.div({"class": "card-body p-0"},
                                                     html.div({"class": "row"},
                                                              html.div({
                                                                  "class": "col-lg-6 d-none d-lg-block bg-login-image"}, ),
                                                              html.div({"class": "col-lg-6"},
                                                                       html.div({"class": "p-5"},
                                                                                html.div(
                                                                                    {"class": "text-center"},
                                                                                    html.h1({
                                                                                        "class": "h4 text-gray-900 mb-4"},
                                                                                        "Welcome Back!"),
                                                                                ),
                                                                                html.form({"class": "user"},
                                                                                          html.div({
                                                                                              "class": "form-group"},
                                                                                              html.input({
                                                                                                  "type": "email",
                                                                                                  "class": "form-control form-control-user",
                                                                                                  "id": "exampleInputEmail",
                                                                                                  "aria-describedby": "emailHelp",
                                                                                                  "placeholder": "Enter Email Address..."
                                                                                              })
                                                                                          ),
                                                                                          html.div({
                                                                                              "class": "from-group"},
                                                                                              html.input({
                                                                                                  "type": "password",
                                                                                                  "class": "form-control form-control-user",
                                                                                                  "id": "exampleInputPassword",
                                                                                                  "placeholder": "Password"
                                                                                              })
                                                                                          ),
                                                                                          html.div({
                                                                                              "class": "form-group"},
                                                                                              html.div({
                                                                                                  "class": "custom-control custom-checkbox small"},
                                                                                                  html.input(
                                                                                                      {
                                                                                                          "type": "checkbox",
                                                                                                          "class": "custom-control-input",
                                                                                                          "id": "customCheck"}),
                                                                                                  html.label(
                                                                                                      {
                                                                                                          "class": "custom-control-label",
                                                                                                          "for": "customCheck"},
                                                                                                      "Remember Me")
                                                                                              ),
                                                                                          ),
                                                                                          html.a({
                                                                                              "href": "index.html",
                                                                                              "class": "btn btn-primary btn-user btn-block"},
                                                                                              "Login"),
                                                                                          html.hr(),
                                                                                          html.a({
                                                                                              "href": "index.html",
                                                                                              "class": "btn btn-google btn-user btn-block"},
                                                                                              html.i({
                                                                                                  "class": "fab fa-google fa-fw"}),
                                                                                              "Login with Google"
                                                                                          ),
                                                                                          html.a({
                                                                                              "href": "index.html",
                                                                                              "class": "btn btn-facebook btn-user btn-block"},
                                                                                              html.i({
                                                                                                  "class": "fab fa-facebook-f fa-fw"}),
                                                                                              "Login with Facebook"
                                                                                          )
                                                                                          ),
                                                                                html.hr(),
                                                                                html.div(
                                                                                    {"class": "text-center"},
                                                                                    html.a({"class": "small",
                                                                                            "href": "#"},
                                                                                           "Forgot Password?")
                                                                                ),
                                                                                html.div(
                                                                                    {"class": "text-center"},
                                                                                    html.a({"class": "small",
                                                                                            "href": "#"},
                                                                                           "Create an Account!")
                                                                                )
                                                                                )
                                                                       )
                                                              )
                                                     )
                                            )
                                   )
                          )
                 )
    )
