from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = useraccount
        fields = ['firstname', 'lastname', 'email', 'phonenumber', 'role', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

