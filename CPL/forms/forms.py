from django import forms
from django.forms import ModelForm

from CPL.models import User


class RideMemberForm(ModelForm):
    full_name = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailField())

    class Meta:
        model = User
        fields = ['full_name', 'email']
