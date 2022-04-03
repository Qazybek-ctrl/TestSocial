from django.forms import ModelForm, TextInput, widgets

from django.contrib.auth.models import User

class RegForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'email' ,
            'first_name',
            'last_name' ,
            'password'
        ]

        widgets = {
            'email' : TextInput(attrs={
                'class':"input100", 
                'type':"text", 
                'name':"email", 
                'placeholder':"Email"
            }),
            'first_name' : TextInput(attrs={
                'class':"input100", 
                'type':"text", 
                'name':"first_name", 
                'placeholder':"First Name"
            }),
            'last_name' : TextInput(attrs={
                'class':"input100", 
                'type':"text", 
                'name':"last", 
                'placeholder':"Last Name"
            }),
            'password' : TextInput(attrs={
                'class':"input100", 
                'type':"password", 
                'name':"pass", 
                'placeholder':"Password"
            })
        }

class LogForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password'
        ]
        widgets = {
            'email' : TextInput(attrs={
                'class':"input100",
                'type':"text", 
                'name':"email", 
                'placeholder':"Email"
            }),
            'password' : TextInput(attrs={
                'class':"input100",
                'type':"password", 
                'name':"pass", 
                'placeholder':"Password"
            })
        }