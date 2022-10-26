from django import forms
from .models import Response

class ResponseCreateForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ("name", "text")