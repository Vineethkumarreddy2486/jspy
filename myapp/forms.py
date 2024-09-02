from django import forms
class Register(forms.Form):
    name=forms.CharField(max_length=26)
    age=forms.IntegerField()