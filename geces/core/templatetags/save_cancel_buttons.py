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


@register.inclusion_tag("templatetags/save_cancel_buttons.html", takes_context=True)
def save_cancel_buttons(context, *args, **kwargs):
    link_back = kwargs.get("link_back", None)  # Pode ser None se 'link_back' não estiver definido nos kwargs
    link_forward = kwargs.get("link_forward", None)  # Pode ser None se 'link_forward' não estiver definido nos kwargs
    has_form = kwargs.get("has_form", False)  # Por padrão, assumimos que não é uma página com formulário

    return {
        "link_back": link_back,
        "link_forward": link_forward,
        "has_form": has_form,
    }
