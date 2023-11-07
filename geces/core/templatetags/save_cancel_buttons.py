from django import template

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
    link_back = kwargs.get("link_back", None)
    link_forward = kwargs.get("link_forward", None)
    has_form = kwargs.get("has_form", False)

    return {
        "link_back": link_back,
        "link_forward": link_forward,
        "has_form": has_form,
    }
