from django import forms

class ShipForm(forms.Form):
    ship_type = forms.CharField(label='Shipment Type', widget=forms.TextInput)
    ship_detail = forms.CharField(label='Shipment Detail', widget=forms.TextInput)
    address = forms.CharField(label='Address', widget=forms.TextInput)

    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
class PayForm(forms.Form):
    pay_Type = forms.CharField(label='Payment Type', widget=forms.TextInput)
    card_num = forms.CharField(label='Card Number', widget=forms.TextInput)
    card_date = forms.DateField(label='Expire Date', widget=forms.DateInput)

    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
