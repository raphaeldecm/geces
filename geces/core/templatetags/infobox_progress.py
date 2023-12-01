from django import template
from django.urls import reverse_lazy

register = template.Library()

"""
Tag criada para 2 botões: save and cancel.

Keywords:
link_back ou url_back -- link do botāo de voltar
link_edit ou link_edit -- link do botāo de editar
delete -- true ou false para indicar que há um botāo de voltar
"""


@register.inclusion_tag("templatetags/infobox_progress.html", takes_context=True)
def infobox(context, *args, **kwargs):
    color = kwargs.get("color", "gradient-success")
    icon = kwargs.get("icon", None)
    header1 = kwargs.get("header1", None)
    header2 = kwargs.get("header2", None)
    subtitle1 = kwargs.get("subtitle1", None)
    subtitle2 = kwargs.get("subtitle2", None)
    number = kwargs.get("number", 0)
    percent = kwargs.get("percent", 0)
    how_long = kwargs.get("how_long", 0)
    link = kwargs.get("link", None)

    if "link" in kwargs:
        k = {}
        link = reverse_lazy(kwargs.get("link"), kwargs=k)

    return {
        "color": color,
        "icon": icon,
        "header1": header1,
        "header2": header2,
        "subtitle1": subtitle1,
        "subtitle2": subtitle2,
        "number": number,
        "percent": percent,
        "how_long": how_long,
        "link": link,
    }
