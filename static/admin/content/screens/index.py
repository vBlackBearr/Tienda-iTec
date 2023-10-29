from reactpy import component, html
from static.admin.content.base.head import head
from reactpy.core.hooks import use_context

# content
from static.admin.content.components.login import login
from static.admin.content.screens._base import Base


@component
def Index(context):
    context_value = use_context(context)

    return Base((login), context_value)