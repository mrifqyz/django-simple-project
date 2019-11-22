from django import forms

class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control width-50vw',
        'id':'user',
        'placeholder': 'Example: coniyz',
        'name':'user'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control width-50vw',
        'id':'pswd',
        'placeholder': '********',
        'name':'pswd'
    }))