from fastapi.staticfiles import StaticFiles

# admin
# --------------------------------------------
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html
from reactpy.core.hooks import create_context
from reactpy_router import route, simple, use_params

# Screens Admin
from admin.content.screens.index import Index as AdminIndex
from admin.content.screens.Partners import Partners as AdminPartners
from admin.content.screens.RawMaterials import RawMaterials
from admin.content.screens.Products import Products as AdminProducts
from admin.content.screens.Sales import Sales
from admin.content.screens.SalesDetails import SalesDetails
from admin.content.screens.Purchases import Purchases
from admin.content.screens.PurchasesLogistica import PurchasesLogistica
from admin.content.screens.SalesLogistica import SalesLogistica
from admin.content.screens.Management import Management

# Screens Shop
from static.screens.index import Index
from static.screens.login import Login
from static.screens.product import Product
from static.screens.cart import Cart
from static.screens.payment import Payment

# routers admin
from api_db.cruds.controllers.controllerPartners import router as router_partners
from api_db.cruds.controllers.controllerRawMaterials import router as router_raw_materials
from api_db.cruds.controllers.controllerProducts import router as router_products
from api_db.cruds.controllers.controllerRoles import router as router_roles
from api_db.cruds.controllers.controllerUsers import router as router_users
from api_db.cruds.controllers.controllerSaleState import router as router_sale_states
from api_db.cruds.controllers.controllerSales import router as router_sales
from api_db.cruds.controllers.controllerProductsSales import router as router_products_sales
from admin.content.endp.pedidos import router as router_pedidos




# routers shop
# from static.cruds.controllers.controllerRoles import router as router_roles

# Database
from api_db.database import get_db


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/api_db", StaticFiles(directory="api_db"), name="api_db")
app.mount("/admin/content", StaticFiles(directory="admin/content"), name="admin")
app.mount("/red_neuronal", StaticFiles(directory="red_neuronal"), name="red_neuronal")
# app.mount("/admin/sales_details", StaticFiles(directory="admin/content"), name="admin")


@component
def App():
    context = create_context({
        "DB": get_db()
    })

    return simple.router(
        route("/", Index(context)),
        route("/login", Login(context)),
        route("/product", Product(context)),
        route("/cart", Cart(context)),
        route("/payment", Payment(context)),


        # Admin
        route("/admin/index", AdminIndex(context)),
        route("/admin/partners", AdminPartners(context)),
        route("/admin/raw_materials", RawMaterials(context)),
        route("/admin/products", AdminProducts(context)),
        route("/admin/sales", Sales(context)),
        route("/admin/sales_details/{id:int}", SalesDetails(context)),
        route("/admin/purchases", Purchases(context)),
        route("/admin/purchases_logistica", PurchasesLogistica(context)),
        route("/admin/sales_logistica", SalesLogistica(context)),
        route("/admin/management", Management(context)),

        route("*", html.h1("Missing Link 🔗‍💥")),
    )


# routers shop
# app.include_router(router_roles)

# routers admin
app.include_router(router_partners)
app.include_router(router_raw_materials)
app.include_router(router_products)
app.include_router(router_sales)
app.include_router(router_products_sales)
app.include_router(router_pedidos)
app.include_router(router_roles)
app.include_router(router_users)
app.include_router(router_sale_states)


configure(app, App)

# uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
