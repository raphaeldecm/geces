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


@register.inclusion_tag("templatetags/infobox.html", takes_context=True)
def infobox(context, *args, **kwargs):

    color = kwargs.get("color", "gradient-success")
    number = kwargs.get("number", 0)
    text = kwargs.get("text", None)
    icon = kwargs.get("icon", None)
    link = kwargs.get("link", None)

    if "link" in kwargs:
        k = {}
        link = reverse_lazy(kwargs.get("link"), kwargs=k)

    return {
        "color": color,
        "number": number,
        "text": text,
        "icon": icon,
        "link": link,
    }
