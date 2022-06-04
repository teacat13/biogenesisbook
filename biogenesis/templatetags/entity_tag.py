from django import template
from biogenesis.models import Vid

register = template.Library()

@register.simple_tag()
def get_vids():
    return Vid.objects.all()
