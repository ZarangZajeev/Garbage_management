from django import forms
from my_work.models import *


class UserGarbageBinForm(forms.ModelForm):
    class Meta:
        model = UserGarbageBin
        fields = [ 'bin']


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['issue']

class userform(forms.ModelForm):
    class Meta:
        model=RequestTable
        fields=["reason"]









