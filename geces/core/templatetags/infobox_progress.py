from django import template
from django.urls import reverse

register = template.Library()


@register.inclusion_tag("templatetags/infobox_progress.html", takes_context=True)
def infobox(context, *args, **kwargs):
    color = kwargs.get("color", "gradient-success")
    icon = kwargs.get("icon", None)
    header1 = kwargs.get("header1", None)
    header2 = kwargs.get("header2", None)
    header3 = kwargs.get("header3", None)
    subtitle1 = kwargs.get("subtitle1", None)
    subtitle2 = kwargs.get("subtitle2", None)
    number = kwargs.get("number", 0)
    percent = kwargs.get("percent", 0)
    how_long = kwargs.get("how_long", 0)
    link = kwargs.get("link", None)

    if "link" in kwargs and kwargs["link"] is not None:
        link = reverse(kwargs["link"], kwargs={'pk': kwargs.get("pk")})

    return {
        "color": color,
        "icon": icon,
        "header1": header1,
        "header2": header2,
        "header3": header3,
        "subtitle1": subtitle1,
        "subtitle2": subtitle2,
        "number": number,
        "percent": percent,
        "how_long": how_long,
        "link": link,
    }
