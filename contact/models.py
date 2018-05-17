from django.db import models

from .forms import ContactForm

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)

from home.models import StandardPage

class ContactPage(StandardPage):
    """
    Detail for a specific feature.
    """

    email = models.CharField("Business email address",
                            max_length=100,
                            help_text="""The email address that receives submitted forms.""")

    thanks_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Thanks Page',
        help_text='Choose the page with the thanks message that will be shown after the form is sent'
    )
    content_panels = StandardPage.content_panels + [
        FieldPanel('email', classname="full"),
        PageChooserPanel('thanks_page'),
    ]

    # Overrides the context to include base form
    def get_context(self, request):
        context = super(ContactPage, self).get_context(request)
        context['form'] = ContactForm
        return context
