from django import forms

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(max_length=254)

class SetPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput)
