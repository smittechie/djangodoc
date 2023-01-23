from django import forms

from .models import Membership, Group, Person


class PGMPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name']


class PGMGroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['group']


class PGMMemberForm(forms.ModelForm):
    person = forms.CharField(max_length=60)

    class Meta:
        model = Membership
        fields = ['person', 'date_joined', 'invite_reason']
