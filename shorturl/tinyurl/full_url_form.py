from django import forms

class FullUrlFrom(forms.Form):
    url = forms.CharField(label='Введите ваш URL', max_length=100)