from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User 
from django import forms 
from .models import post 


class Signup(UserCreationForm):
    password1 = forms.CharField(label='Password' , widget=forms.PasswordInput(attrs={
        'class' : 'form-control'
    }
    ))
    password2 = forms.CharField(label='confirm password(again password) ! ' , widget=forms.PasswordInput(attrs={
        'class' : 'form-control'
        
    })
    )
    class Meta:
        model = User
        fields = ['username' ,  'first_name' ,'last_name' , 'email']
        labels = {'first_name' : 'First Name' , 'last_name' : 'Last Name' , 'email' : 'Email'}

        widgets = {'password1' :  forms.PasswordInput(attrs={
            'class' :'form-control',
            'id' : 'form-control'
        }) , 
        'username' : forms.TextInput(attrs={
            'class' : 'form-control'
        }),
        'first_name' : forms.TextInput(attrs={
            'class' : 'form-control'
        }),
        'last_name' : forms.TextInput(attrs={
            'class' : 'form-control'
        }),
        'email' : forms.EmailInput(attrs={
            'class' : 'form-control'
        }),
        }


class SigninUser(AuthenticationForm):
    username = forms.CharField( required=True , widget=forms.TextInput(attrs={'autofocus' : True  , 'class' : 'form-control'}))
    password = forms.CharField(  required=True ,label="password" , strip=False , widget=forms.TextInput(attrs={'autocomplete' :'current-password', 'class' : 'form-control'}))




#-----------------------------------create post form --------------------------

class create_post(forms.ModelForm):
    
    class Meta:
        model = post
        fields = ("title","desc")
        widgets = {'title' : forms.TextInput(attrs={
            'class': 'form-control',
            'autofocus' : True
        }),
        "desc" : forms.Textarea(attrs={"autofocus": True ,
        "class" : "form-control"})}
