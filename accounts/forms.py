

from django import forms
from django.contrib.auth.models import User
from .models import Profile

class RegistrationForm(forms.ModelForm):
    username= forms.CharField(label='Username', max_length=250,help_text='',required=True, widget=forms.TextInput(attrs={
        'class':"form-control", 'id':"username" , 'type':"text", 'placeholder':"Username", 'data-sb-validations':"required"
    }))
    Fist_name= forms.CharField(label='Fist Name', max_length=250,help_text='',required=True, widget=forms.TextInput(attrs={
        'class':"form-control", 'id':"Fist_name" , 'type':"text", 'placeholder':"Fist_name", 'data-sb-validations':"required"
    }))
    
    last_name= forms.CharField(label='last Name', max_length=250,help_text='',required=True, widget=forms.TextInput(attrs={
        'class':"form-control", 'id':"last_name" , 'type':"text", 'placeholder':"last_name", 'data-sb-validations':"required"
    }))
    email= forms.EmailField(label='Email', max_length=250,help_text='',required=True, widget=forms.EmailInput(attrs={
        'class':"form-control", 'id':"email" , 'type':"email", 'placeholder':"email", 'data-sb-validations':"required"
    }))
    password= forms.CharField(label='Password', max_length=250,help_text='',required=True, widget=forms.PasswordInput(attrs={
        'class':"form-control", 'id':"password" , 'type':"password", 'placeholder':"password", 'data-sb-validations':"required"
    }))
    confirm_password= forms.CharField(label='confirm_password', max_length=250,help_text='',required=True, widget=forms.PasswordInput(attrs={
        'class':"form-control", 'id':"confirm_password" , 'type':"password", 'placeholder':"confirm_password", 'data-sb-validations':"required"
    }))
    class Meta:
        model = User
        fields =('username','first_name','last_name','email','password',)
        
        
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     confirm_password = cleaned_data.get('confirm_password')

    #     if password and confirm_password and password != confirm_password:
    #         raise forms.ValidationError("Passwords don't match")

    #     return cleaned_data    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_img']    