from django import template
from apps.forms import Search
register = template.Library()
from apps.models import Cathegorie, Mark


@register.inclusion_tag("widgets/filter.html")
def filter():
    return {'cathegories': Cathegorie.objects.all(),
                  'marks': Mark.objects.all()}


