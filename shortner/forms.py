from django import forms

class Urlform(forms.Form):
    url=forms.URLField(label='url',max_length=200)
