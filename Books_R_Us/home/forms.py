from django import forms
from django.contrib.auth.models import User

#Creating new SELLER account
class SellerReg(forms.Form):
    email = forms.EmailField()
    username=forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Passwords do not match. Please enter the same password in both fields."
            )
        return cleaned_data
#Login to SELLER account
class SellerLogForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField()

#Creating new BUYER account
class BuyerReg(forms.Form):
    email = forms.EmailField()
    username=forms.CharField(max_length=100)
    password = forms.CharField()

    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Passwords do not match. Please enter the same password in both fields."
            )
        return cleaned_data
#Login to new BUYER account
class BuyerLogForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField()

#Update BUYER account
class BuyerUpdate(forms.Form):
    new_username=forms.CharField(label='New Username', max_length=100)

#Update SELLER account
class SellerUpdate(forms.Form):
    new_username=forms.CharField(label='New Username', max_length=100)

class SearchForm(forms.Form):
    query = forms.CharField()

class AdminLogForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField()