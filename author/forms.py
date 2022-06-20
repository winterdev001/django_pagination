from django import forms

class AuthorForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
