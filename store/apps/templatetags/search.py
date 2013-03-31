from django import template
from apps.forms import Search
register = template.Library()

@register.inclusion_tag("widgets/search_form.html")
def search():
    search_form = Search()
    return {"search":search_form}


