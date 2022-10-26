from django import forms
from .models import Response

class ResponseCreateForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ("name", "email", "text", "delete_code")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["delete_code"].widget = forms.HiddenInput()