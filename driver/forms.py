from django import forms
from my_work.models import CollectionRequest


class RquestForm(forms.ModelForm):
    class Meta:
        model = CollectionRequest
        fields = ["area","bin","created_at"]