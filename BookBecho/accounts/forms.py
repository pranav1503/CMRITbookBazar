from django import forms
from django.contrib.auth.models import User
from .models import UserInfoModel,UserInfo

class UserForm(forms.ModelForm):

    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class' : 'reg-textbox',
            'placeholder' : 'Email(CMRIT E-Mail)'
        }
    ),label='')
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'reg-textbox',
            'placeholder' : 'Username'
        }
    ),label='')
    password = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'reg-textbox',
            'type' : 'password',
            'placeholder' : 'Password'
        }
    ),label='')
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'reg-fln',
            'placeholder' : 'First Name'
        }
    ),label='')
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'reg-fln',
            'placeholder' : 'Last Name'

        }
    ),label='')
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']

class PhoneForm(forms.ModelForm):
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'reg-textbox',
            'placeholder' : 'Mobile Number'
        }
    ),label='')
    class Meta:
        model = UserInfo
        fields = ['phone_number']
