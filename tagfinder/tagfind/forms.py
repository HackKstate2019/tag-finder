from django import forms

class UrlForm(forms.Form):
    url = forms.URLField(max_length=None, required=True, label='', widget=forms.TextInput(attrs={"placeholder":"Insert link here."}))