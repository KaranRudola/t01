from django import forms
from .models import SysUser
from django.contrib.auth.hashers import make_password

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password"
    )

    class Meta:
        model = SysUser
        fields = ['employee_number', 'full_name', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        # Hash the plain password into password_hash
        user.password_hash = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user