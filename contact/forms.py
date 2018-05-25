from django import forms
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(label=_('Your name'),
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label=_('Your email'),
                            max_length=100,
                            widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label=_("Phone"),
                            max_length=100,
                            required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label=_('Message'),
                              max_length=500,
                              widget=forms.Textarea(attrs={'class': 'form-control'}))
