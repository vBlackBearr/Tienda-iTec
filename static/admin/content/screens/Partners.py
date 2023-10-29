from reactpy import component
from reactpy.core.hooks import use_context

# content
from static.admin.content.cruds.views.partnersCrud import PartnersCrud
from static.admin.content.screens._base import Base


@component
def Partners(context):
    context_value = use_context(context)

    return Base((
        PartnersCrud()
    ), context_value)
