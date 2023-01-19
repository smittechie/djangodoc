from django import forms

from .models import Person, Fruits


class ShirtForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class FruitsForm(forms.ModelForm):
    class Meta:
        model = Fruits
        fields = '__all__'