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

@register.inclusion_tag('templatetags/save_cancel_buttons.html', takes_context=True)
def save_cancel_buttons(context, *args, **kwargs):

    link_back = kwargs.get("link_back")

    if "url_back" in kwargs:
        k = {}
        link_back = reverse_lazy(kwargs.get("url_back"), kwargs=k)

    print(link_back)
    return {
        "link_back": link_back,
    }
