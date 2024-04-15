from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext, gettext_lazy as _

class SignUpForm(UserCreationForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[validate_password],  # Keep basic password validation
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ('name', 'email', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # Remove specific password validation constraints
        self.fields['password1'].validators = []

        # Set field labels
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'

        # Update widget attributes
        for field_name in ('username', 'email', 'password1', 'password2'):
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
