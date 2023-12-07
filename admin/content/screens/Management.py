from reactpy import component
from reactpy.core.hooks import use_context

# content
from admin.content.cruds.views.salesCrud import SalesCrud
from admin.content.screens._base import Base


@component
def Management(context):
    context_value = use_context(context)

    return Base((



    ), context_value)
