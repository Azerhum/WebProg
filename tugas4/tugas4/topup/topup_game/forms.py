from django import forms

class TopUpForm(forms.Form):
    amount = forms.DecimalField(max_digits=8, decimal_places=2, required=True)