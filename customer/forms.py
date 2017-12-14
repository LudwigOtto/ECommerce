from django import forms

class LoginForm(forms.Form):
    c_id = forms.IntegerField(label='User ID', widget=forms.NumberInput)
    email = forms.EmailField(label='E-Mail', widget=forms.EmailInput)
    phone = forms.CharField(label='Phone #', widget=forms.TextInput)

class RegisterForm(forms.Form):
    c_id = forms.IntegerField(label='User ID', widget=forms.NumberInput)
    email = forms.EmailField(label='E-Mail', widget=forms.EmailInput)
    phone = forms.CharField(label='Phone #', widget=forms.TextInput)
