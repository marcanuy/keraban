from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.CharField(label='Your email', max_length=100)
    phone = forms.CharField(label="Business email address",
                             max_length=100,
                             required=False)

    message = forms.CharField(label='Message', max_length=500)
