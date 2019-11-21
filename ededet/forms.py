from django import forms

class StatusForm(forms.Form):
    status = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-style',
        'placeholder': 'Jawaban kamu...'
    }), label='',)

