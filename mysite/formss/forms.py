from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms import Textarea

from .models import TITLE_CHOICES, Author


class NameForm(forms.Form):
    yourname = forms.CharField(label="Your name", max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


# class AuthorForm(forms.Form):
#     name = forms.CharField(max_length=20)
#     title = forms.CharField(max_length=3,
#                             widget=forms.Select(choices=TITLE_CHOICES), )
#     birth_date = forms.DateField(required=True)
#
#
#     # def clean(self):                                            ## all validation
#     #     cleaned_data = super().clean()
#     #     name = cleaned_data.get("name")
#     #     if  self.cleaned_data['name']:
#     #         raise ValidationError(
#     #             "Did not send for 'help' in the subject despite "
#     #             "CC'ing yourself.")
#
#     def clean_name(self):                                       ## specific field validation
#         data = self.cleaned_data['name']
#         if 'smit' in data:
#             raise ValidationError("check the item ")

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())

#
# class AuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ['name', 'title', 'birth_date']
#
# class BookForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = ['name', 'authors']