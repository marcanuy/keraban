from django import forms
from django.db import models

from collections import defaultdict

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Collection, Page
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from modelcluster.fields import ParentalManyToManyField

from home.choices import CONTACT_TYPES_CHOICES

@register_snippet
class SocialProfiles(models.Model):
    """
    Business Social Profile links
    """
    name = models.CharField(max_length=255, help_text="name of the social network")
    url = models.URLField(help_text="Example: https://facebook.com/my-business-page")
    icon = models.CharField(max_length=20, help_text="fontawesome icon of the social network. Ex: fa-facebook")
    
    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
        FieldPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Social networks'

@register_snippet
class ContactNumbers(models.Model):
    """
    Implementation of Schema.org's ContactPoint main attributes
    http://schema.org/ContactPoint
    """
    telephone = models.CharField(max_length=20, help_text="Telephone number. Ex.: +1-877-296-1018")
    contact_type = models.CharField(
        max_length=2,
        choices=CONTACT_TYPES_CHOICES,
        default='GRID'
    )
    area_served = models.CharField(
        max_length=2,
        help_text='The geographical region served by the number, specified as a AdministrativeArea. Countries may be specified concisely using just their standard ISO-3166 two-letter code, as in the examples below. If omitted, the number is assumed to be global. Examples: "US", "GB", ["US","CA","MX"]',
        null=True,
        blank=True)
    available_language = models.CharField(
        max_length=20,
        help_text='Details about the language spoken. Languages may be specified by their common English name. If omitted, the language defaults to English. Examples: "English", "Spanish", ["French","English"]',
        null=True,
        blank=True)
    panels = [
        FieldPanel('telephone'),
        FieldPanel('contact_type'),
        FieldPanel('area_served'),
        FieldPanel('available_language'),
    ]

    # https://docs.djangoproject.com/en/2.0/ref/models/instances/#django.db.models.Model.get_FOO_display
    # def get_contact_type_display()

    def get_available_language_as_list(self):
        al = self.available_language
        return al.split(',')
    
    def __str__(self):
        return self.telephone

    class Meta:
        verbose_name_plural = 'Contact Points'


@register_snippet
class Organization(models.Model):
    """
    This provides editable text for the site business info. Uses the decorator
    `register_snippet` to allow it to be accessible via the admin. It is made
    accessible on the template via a template tag defined in base/templatetags/
    navigation_tags.py
    This sets:
        - schema.org Organization and LocalBusiness metadata
        - footer business data text
        - contact pages phone and business data
    See also Googles knowledge panel: https://support.google.com/business/answer/3039617
    Data for:
      Organization: https://schema.org/Organization
          Business Name
          URL
          Social Profile Links
      Local Business: http://schema.org/LocalBusiness
          Business Name
          URL
          Logo
          Description
          Telephone
          Address Locality
          Address Region
          Street Address
          Opening Hours
    """
    name = models.CharField("Business name",
                            max_length=100,
                            null=True,
                            blank=True,
                            help_text="""The name of your business that will appear on Google.""")

    email = models.CharField("Business email address",
                            max_length=100,
                            null=True,
                            blank=True,
                            help_text="""The email of your business.""")

    address = models.TextField(null=True,
                               blank=True,
                               help_text=""" Comma separated list with the following format:<street address>,<address locality (city)>, <address region>,<postal code>,<address country (two letters)>. Ex.: 1901 Lemur Ave, Sunnyvale, CA, 94086, US """)

    hours = models.TextField(null=True,
                             blank=True,
                             help_text=
                             """ """)
    phone = models.TextField(null=True,
                             blank=True,
                             help_text=""" """)

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )

    description = models.TextField(null=True,
                                   blank=True,
                                   help_text=""" From the business """)

    #body = RichTextField()

    geo_coordinates = models.TextField(null=True,
                                       blank=True,
                                       help_text=
                                       """Comma separated geo coordinates as <latitude,longitude>. Es: -34.8844053,-56.1609289""")

    contact_points = models.ManyToManyField('ContactNumbers', blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('email'),
        FieldPanel('address'),
        FieldPanel('hours'),
        FieldPanel('phone'),
        FieldPanel('description'),
        FieldPanel('geo_coordinates'),
        ImageChooserPanel('image'),
        FieldPanel('contact_points', widget=forms.CheckboxSelectMultiple)
    ]

    def address_as_list(self):
        return self.address.split(',')

    def phone_as_list(self):
        return self.phone.split(',')

    def geo_coordinates_as_list(self):
        return self.geo_coordinates.split(',')

    def __str__(self):
        return "Business text"

    class Meta:
        verbose_name_plural = 'Organization'


class StandardPage(Page):
    """
    A generic content page. All other pages inherits extend this class.
    """
    subtitle = models.CharField(
        max_length=255,
        help_text='Write a subtitle for the page',
        null=True,
        blank=True,
    )
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=''
    )

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title", required=False)),
        ('paragraph', blocks.RichTextBlock(required=False)),
        ('image', ImageChooserBlock(required=False)),
    ],                             null=True,
                            blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname="full"),
        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]

class HomePage(Page):
    """
    The Home Page.

    (based on bakery wagtail demo)
    """

    # Hero section of HomePage
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Homepage image'
    )
    hero_text = models.CharField(
        max_length=255,
        help_text='Write an introduction for the business'
        )
    hero_cta = models.CharField(
        verbose_name='Hero CTA',
        max_length=255,
        help_text='Text to display on Call to Action'
        )
    hero_cta_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Hero CTA link',
        help_text='Choose a page to link to for the Call to Action'
    )

    # Featured sections on the HomePage
    featured_section_1_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    featured_section_1 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='First featured section for the homepage. Will display up to '
        'three child items.',
        verbose_name='Featured section 1'
    )

    featured_section_2_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )
    featured_section_2 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Second featured section for the homepage. Will display up to '
        'three child items.',
        verbose_name='Featured section 2'
    )

    featured_features = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Features section.',
        verbose_name='Featured features page'
    )

    featured_location = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Location section.',
        verbose_name='Featured location page at homepage'
    )

    featured_gallery = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Gallery section.',
        verbose_name='Gallery section at homepage'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('image'),
            FieldPanel('hero_text', classname="full"),
            MultiFieldPanel([
                FieldPanel('hero_cta'),
                PageChooserPanel('hero_cta_link'),
                ])
            ], heading="Hero section"),
        MultiFieldPanel([
            MultiFieldPanel([
                FieldPanel('featured_section_1_title'),
                PageChooserPanel('featured_section_1'),
                ]),
            MultiFieldPanel([
                FieldPanel('featured_section_2_title'),
                PageChooserPanel('featured_section_2'),
                ]),
            PageChooserPanel('featured_features'),
            PageChooserPanel('featured_gallery'),
            PageChooserPanel('featured_location'),
        ], heading="Featured homepage sections", classname="collapsible")
    ]

    def __str__(self):
        return self.title
