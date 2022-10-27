from django import forms
from .models import Thread, Response

class ThreadCreateForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ("title",)

class ResponseCreateForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ("name", "email", "text")

    """ def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["delete_code"].widget = forms.HiddenInput() """