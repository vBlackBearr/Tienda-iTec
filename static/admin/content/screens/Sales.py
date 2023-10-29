from reactpy import component
from reactpy.core.hooks import use_context

# content
from static.admin.content.cruds.views.salesCrud import SalesCrud
from static.admin.content.screens._base import Base


@component
def Sales(context):
    context_value = use_context(context)

    return Base((
        SalesCrud()
    ), context_value)
