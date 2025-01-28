from django import template

register = template.Library()

@register.filter
def get_item(obj, key):
    return getattr(obj, key, None)
