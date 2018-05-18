# from datetime import datetime

# from django.conf import settings
# from django.core.validators import RegexValidator
from django.db import models

# from modelcluster.fields import ParentalKey

# from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.core.models import Collection #, Orderable, Page
# from wagtail.search import index
# from wagtail.images.edit_handlers import ImageChooserPanel

from home.models import StandardPage
from gallery.choices import GALLERY_CHOICES

class GalleryIndexPage(StandardPage):
    """
    A Page model that creates an index page (a listview)
    """

    # Only GalleryPage objects can be added underneath this index page
    subpage_types = ['GalleryPage']

    # Allows children of this indexpage to be accessible via the indexpage
    # object on templates. We use this on the homepage to show featured
    # sections of the site and their child pages
    def children(self):
        return self.get_children().specific().live()

    # Overrides the context to list all child
    # items, that are live, by the date that they were published
    # http://docs.wagtail.io/en/latest/getting_started/tutorial.html#overriding-context
    def get_context(self, request):
        context = super(GalleryIndexPage, self).get_context(request)
        context['galleries'] = GalleryPage.objects.descendant_of(
            self).live().order_by(
            'title')
        return context


class GalleryPage(StandardPage):
    """
    Detail for a specific gallery.
    """

    galery_type = models.CharField(
        max_length=4,
        choices=GALLERY_CHOICES,
        default='GRID'
    )

    collection = models.ForeignKey(
        Collection,
        limit_choices_to=~models.Q(name__in=['Root']),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text='Select the image collection for this gallery.'
    )

    # Fields to show to the editor in the admin view
    content_panels = StandardPage.content_panels + [
        FieldPanel('collection', classname="full"),
        FieldPanel('galery_type'),
    ]

    def __str__(self):
        return self.title

