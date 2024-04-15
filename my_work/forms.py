from django import forms
from my_work.models import *
from django.contrib.auth.forms import AuthenticationForm
from my_work.models import User

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Phone', max_length=13)

    class Meta:
        model = User
        fields = ['username', 'password']

  


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =["full_name","phone","email","address","password","user_type","location"]
        read_only_fields=["is_active","is_staff"]

class GarbageBinForm(forms.ModelForm):
    class Meta:
        model = GarbageBin
        fields = ['name', 'price']


class AddLocationForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = "__all__"








