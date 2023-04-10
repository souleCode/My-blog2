

from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    username= forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    
    email= forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))
    body= forms.CharField(max_length=255,widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    class Meta:
        model = Comment
        fields =[
            'username','email','body',
        ]
        
class SearchPost(forms.Form):
    query= forms.CharField(max_length=255)
    
    class Meta:
        
        fields= ('query',)
            