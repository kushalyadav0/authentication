from django import forms
from .models import SignUp

class SignUp_form(forms.ModelForm):

    class Meta:
        model = SignUp
        fields = ('username', 'email', 'password', )