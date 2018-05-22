from django import template
from django.conf import settings

from wagtail.core.models import Page
from home.models import SocialProfiles, Organization

register = template.Library()
# https://docs.djangoproject.com/en/2.0/howto/custom-template-tags/

@register.simple_tag
def get_base_url():
    #return getattr(settings, "BASE_URL", "")
    return settings.BASE_URL

@register.simple_tag
def get_business_name():
    name = ""
    if Organization.objects.first() is not None:
        name = Organization.objects.first().name
    return name

@register.inclusion_tag('tags/footer_business_data.html', takes_context=True)
def get_footer_business_data(context):
    business = ""
    profiles = SocialProfiles.objects.all()
    if Organization.objects.first() is not None:
        business = Organization.objects.first()
    return {
        'site_root': context['request'].site.root_page,
        'business': business,
        'profiles': profiles
    }

@register.inclusion_tag('tags/business_contact.html', takes_context=True)
def get_business_contact(context):
    business = ""
    if Organization.objects.first() is not None:
        business = Organization.objects.first()
    return {'business': business}
