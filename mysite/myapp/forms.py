from django import forms

from .models import Person, Fruits, Person1, Group, Membership


class ShirtForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class FruitsForm(forms.ModelForm):
    class Meta:
        model = Fruits
        fields = '__all__'


class PGMPersonForm(forms.ModelForm):
    class Meta:
        model = Person1
        fields = ['name']

class PGMGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class PGMMemberForm(forms.ModelForm):
    person1 = forms.CharField(max_length=60)
    class Meta:
        model = Membership
        fields = ['person1', 'date_joined', 'invite_reason']