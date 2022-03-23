from django import forms

TONTINES_LIST = [
    ("52 USDT", "Tontine 52 USDT"),
    ("302 USDT", "Tontine 302 USDT"),
    ("502 USDT", "Tontine 502 USDT"),
    ("1002 USDT", "Tontine 1002 USDT"),
    ("2002 USDT", "Tontine 2002 USDT")
]

class TontineForm(forms.Form):
    tontine = forms.ChoiceField(choices=TONTINES_LIST, required=True)
    email = forms.EmailField(max_length=255, required=True)
    address = forms.CharField(max_length=255, required=True)
    is_ok = forms.BooleanField(required=True)


