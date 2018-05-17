from datetime import datetime

from django.conf import settings
from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel

from home.models import StandardPage

class FeaturesIndexPage(StandardPage):
    """
    A Page model that creates an index page (a listview)
    """

    # Only FeaturePage objects can be added underneath this index page
    subpage_types = ['FeaturesPage']

    # Allows children of this indexpage to be accessible via the indexpage
    # object on templates. We use this on the homepage to show featured
    # sections of the site and their child pages
    def children(self):
        return self.get_children().specific().live()

    # Overrides the context to list all child
    # items, that are live, by the date that they were published
    # http://docs.wagtail.io/en/latest/getting_started/tutorial.html#overriding-context
    def get_context(self, request):
        context = super(FeaturesIndexPage, self).get_context(request)
        context['features'] = FeaturesPage.objects.descendant_of(
            self).live().order_by(
            'title')
        return context

    # content_panels = Page.content_panels + [
    #     FieldPanel('introduction', classname="full"),
    #     ImageChooserPanel('image'),
    # ]


class FeaturesPage(StandardPage):
    """
    Detail for a specific feature.
    """

    icon = models.TextField(
        help_text='FontAwesome icon to describe the service e.g.: fa-facebook Full list at: https://fontawesome.com/v4.7.0/icons/',
        blank=True)

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = StandardPage.content_panels + [
        FieldPanel('icon', classname="full"),
    ]

    def __str__(self):
        return self.title

    # Can only be placed under a FeaturesIndexPage object
    parent_page_types = ['FeaturesIndexPage']
