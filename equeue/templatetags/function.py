
from django import template
register = template.Library()

@register.simple_tag
def minToHr(minutes):
    return '{:01d} hr  {:02d} min'.format(*divmod(minutes, 60))

