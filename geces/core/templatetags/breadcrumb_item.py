from django import template
from django.urls import reverse_lazy

register = template.Library()


@register.inclusion_tag("templatetags/breadcrumb_item.html")
def breadcrumb_item(*args, **kwargs):

    if "active" not in kwargs:
        active = False
    else:
        active = kwargs.get("active")

    link = kwargs.get("link")

    if "url" in kwargs:
        k = {}
        if "pk" in kwargs:
            k["pk"] = kwargs.get("pk")
        if "itinerary" in kwargs:
            k["itinerary"] = kwargs.get("itinerary")
        if "unit" in kwargs:
            k["unit"] = kwargs.get("unit")

        link = reverse_lazy(kwargs.get("url"), kwargs=k)

    return {
        "text": kwargs.get("text"),
        "link": link,
        "active": active,
    }
