from django import template
from django.conf import settings

from wagtail.images.models import Image

from home.models import Organization

register = template.Library()

@register.inclusion_tag('tags/map.html', takes_context=True)
def show_map(context):
    business = Organization.objects.first()
    pos = business.geo_coordinates.split(',')

    return {
        'address' : business.address,
        'lat' : pos[0],
        'long' : pos[1],
        'google_map_api_key' : settings.GOOGLE_MAP_API_KEY,
        'request': context['request'],
    }
