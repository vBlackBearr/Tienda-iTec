import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from reactpy import component, html
from reactpy_router import route, simple
from reactpy.core.hooks import create_context
from reactpy.backend.fastapi import configure

# admin
# --------------------------------------------
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html
from reactpy.core.hooks import create_context
from reactpy_router import route, simple

# Screens Admin
from static.admin.content.screens.index import Index
from static.admin.content.screens.Partners import Partners
from static.admin.content.screens.RawMaterials import RawMaterials
from static.admin.content.screens.Products import Products
from static.admin.content.screens.Sales import Sales

# Screens Shop
from static.screens.index import Index
from static.screens.login import Login
from static.screens.product import Product
from static.screens.cart import Cart
from static.screens.payment import Payment

# routers admin
from static.admin.content.cruds.controllers.controllerPartners import router as router_partners
from static.admin.content.cruds.controllers.controllerRawMaterials import router as router_raw_materials
from static.admin.content.cruds.controllers.controllerProducts import router as router_products
from static.admin.content.cruds.controllers.controllerSales import router as router_sales
from static.admin.content.endp.pedidos import router as router_pedidos

# routers shop
from static.cruds.controllers.controllerRoles import router as router_roles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@component
def App():
    context = create_context("value")

    return simple.router(
        route("/", Index(context)),
        route("/login", Login(context)),
        route("/product", Product(context)),
        route("/cart", Cart(context)),
        route("/payment", Payment(context)),
        route("*", html.h1("Missing Link 🔗‍💥"))
    )


# routers shop
app.include_router(router_roles)

# routers admin
app.include_router(router_partners)
app.include_router(router_raw_materials)
app.include_router(router_products)
app.include_router(router_sales)
app.include_router(router_pedidos)

configure(app, App)

uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
