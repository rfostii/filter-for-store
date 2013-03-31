from django import template
register = template.Library()


@register.inclusion_tag('ajax/items.html')
def render_data(request):
    pass
