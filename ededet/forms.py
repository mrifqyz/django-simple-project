from django import forms

class StatusForm(forms.Form):
    status = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-style',
        'placeholder': 'Jawaban kamu...'
    }), label='',)

class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-style',
        'placeholder': 'Username'
    }), label='',)

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-style',
        'placeholder': 'Password'
    }))