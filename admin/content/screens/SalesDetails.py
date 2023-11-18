from reactpy import component, html
from reactpy.core.hooks import use_context
from reactpy_router import use_params

# content
from admin.content.cruds.views.salesCrud import SalesCrud
from admin.content.screens._base import Base


@component
def SalesDetails(context):
    app.mount("/admin/content", StaticFiles(directory="admin/content"), name="admin")

    context_value = use_context(context)

    params = use_params()

    return Base((
        html.h1(params["id"])
    ), context_value)
