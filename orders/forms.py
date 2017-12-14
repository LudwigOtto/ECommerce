from django import forms

class ShipForm(forms.Form):
    c_id = forms.IntegerField(label='User ID', widget=forms.NumberInput)
    email = forms.EmailField(label='E-Mail', widget=forms.EmailInput)
    phone = forms.CharField(label='Phone #', widget=forms.TextInput)
    address = forms.CharField(label='Address', widget=forms.TextInput)

    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
class PayForm(forms.Form):
    c_id = forms.IntegerField(label='User ID', widget=forms.NumberInput)
    firstN = forms.CharField(label='First Name', widget=forms.TextInput)
    lastN = forms.CharField(label='Last Name', widget=forms.TextInput)
    email = forms.EmailField(label='E-Mail', widget=forms.EmailInput)
    phone = forms.CharField(label='Phone #', widget=forms.TextInput)
    address = forms.CharField(label='Address', widget=forms.TextInput)

    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
