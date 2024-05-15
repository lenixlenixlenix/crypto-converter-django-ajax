from django import forms

from .functions import CryptoClass


names_list = CryptoClass.return_names()
integer_list = [i for i in range(1,50)]

choices_list = [(i, names_list[i-1]) for i in integer_list]


class CurrencyConverterForm(forms.Form):
    convert_from = forms.ChoiceField(choices=choices_list)
    convert_to = forms.ChoiceField(choices=choices_list)
    amount = forms.IntegerField(max_value=999999, label="AMOUNT")
    converted = forms.IntegerField(max_value=999999, label="CONVERTED")