from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.Form):
    sender = forms.EmailField()
    subject = forms.CharField(min_length=5, max_length=32)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.include_media = True
        self.helper.form_action = '.'
        self.helper.add_input(Submit('submit', 'Send'))

    class Meta:
        widgets = {

        }