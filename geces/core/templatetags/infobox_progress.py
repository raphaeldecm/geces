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
    header = kwargs.get("header", None)
    number = kwargs.get("number", 0)
    unit = kwargs.get("unit", None)
    percent = kwargs.get("percent", 0)
    how_long = kwargs.get("how_long", 0)
    link = kwargs.get("link", None)

    if "link" in kwargs:
        k = {}
        link = reverse_lazy(kwargs.get("link"), kwargs=k)

    return {
        "color": color,
        "icon": icon,
        "header": header,
        "number": number,
        "unit": unit,
        "percent": percent,
        "how_long": how_long,
        "link": link,
    }
