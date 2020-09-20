from django import forms
from shortner.models import UrlData
    

class UrlForm(forms.ModelForm):
    long_url = forms.URLField(max_length=256)
    class Meta:
        model = UrlData
        fields = ['long_url']