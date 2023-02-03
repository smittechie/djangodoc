from django import forms


class NameForm(forms.Form):
    yourname = forms.CharField(label="Your name", max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
