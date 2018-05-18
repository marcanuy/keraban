from django import template

from wagtail.images.models import Image

register = template.Library()

# Retrieves a single gallery item and returns a gallery of images
@register.inclusion_tag('tags/gallery.html', takes_context=True)
def gallery(context, gallery):
    images = Image.objects.filter(collection=gallery)
    return {
        'images': images,
        'request': context['request'],
    }

@register.inclusion_tag('tags/gallery_grid.html', takes_context=True)
def gallery_grid(context, gallery):
    images = Image.objects.filter(collection=gallery)
    return {
        'images': images,
        'request': context['request'],
    }
@register.inclusion_tag('tags/gallery_card.html', takes_context=True)
def gallery_card(context, gallery):
    images = Image.objects.filter(collection=gallery)
    return {
        'images': images,
        'request': context['request'],
    }

@register.inclusion_tag('tags/gallery_compact.html', takes_context=True)
def gallery_compact(context, gallery):
    images = Image.objects.filter(collection=gallery)
    return {
        'images': images,
        'request': context['request'],
    }

@register.inclusion_tag('tags/gallery_index_item.html', takes_context=True)
def gallery_item(context, gallery, limit=None):
    images = Image.objects.filter(collection=gallery)
    if limit:
        images = images[:limit]
    return {
        'images': images,
        'request': context['request'],
    }
