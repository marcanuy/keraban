from django import forms
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(label=_('Your name'), max_length=100)
    email = forms.CharField(label=_('Your email'), max_length=100)
    phone = forms.CharField(label=_("Phone"),
                             max_length=100,
                             required=False)

    message = forms.CharField(label=_('Message'), max_length=500, widget=forms.Textarea)
