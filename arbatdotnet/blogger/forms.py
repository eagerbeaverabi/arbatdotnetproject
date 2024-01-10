from django import forms
from .models import Blogger

class LoginForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
    class Meta:
        model = Blogger
        fields = ['username', 'password']
        labels = {'username':'USERNAME ', 'password':'PASSWORD '}
        widgets = {
            'username' : forms.TextInput(),
            'password' : forms.PasswordInput()
        }
class RegisterationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
    fullname = forms.CharField(widget=forms.TextInput(), label='FULLNAME ')
    username = forms.CharField(widget=forms.TextInput(), label='USERNAME ')
    email = forms.CharField(widget=forms.EmailInput(), label='EMAIL ')
    password = forms.CharField(widget=forms.PasswordInput(), label='PASSWORD ')