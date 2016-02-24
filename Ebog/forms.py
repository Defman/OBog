from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class BookFormCreate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookFormCreate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.include_media = True
        self.helper.form_action = '.'
        self.helper.add_input(Submit('submit', 'Create'))

    class Meta:
        model = Book
        fields = fields = ["title", "tags", "description"]
        widgets = {
        }


class SectionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.include_media = True
        self.helper.form_action = '.'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Section
        fields = '__all__'
        exclude = ['author']
        widgets = {
        }


class PageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.include_media = True
        self.helper.form_action = '.'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Page
        fields = '__all__'
        exclude = ['author']
        widgets = {
        }


class TagForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.include_media = True
        self.helper.form_action = '.'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Tag
        fields = '__all__'
        exclude = ['author']
        widgets = {
        }
