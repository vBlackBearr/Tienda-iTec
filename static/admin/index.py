from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html
from reactpy.core.hooks import create_context
from reactpy_router import route, simple


# content
from static.admin.content.screens.index import Index
from static.admin.content.screens.Partners import Partners
from static.admin.content.screens.RawMaterials import RawMaterials
from static.admin.content.screens.Products import Products
from static.admin.content.screens.Sales import Sales

# routers
from static.admin.content.cruds.controllers.controllerPartners import router as router_partners
from static.admin.content.cruds.controllers.controllerRawMaterials import router as router_raw_materials
from static.admin.content.cruds.controllers.controllerProducts import router as router_products
from static.admin.content.cruds.controllers.controllerSales import router as router_sales
from static.admin.content.endp.pedidos import router as router_pedidos


app = FastAPI()
# por buenas prácticas según se montan así los recursos en fastapi, yo digo que le hacen a la mamada nomás
# x2
# x3 xd


@component
def App():
    context = create_context("value")

    return simple.router(
        route("/", Index(context)),
        route("/partners", Partners(context)),
        route("/raw_materials", RawMaterials(context)),
        route("/products", Products(context)),
        route("/sales", Sales(context)),
        route("*", html.h1("Missing Link 🔗‍💥"))
    )


app.include_router(router_partners)
app.include_router(router_raw_materials)
app.include_router(router_products)
app.include_router(router_sales)
app.include_router(router_pedidos)


configure(app, App)
