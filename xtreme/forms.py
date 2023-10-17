from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[forms.validators.EmailValidator(message='Invalid email address')],
    )
    
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[forms.validators.MinLengthValidator(limit_value=1, message='Password is required')],
    )
    
    remember_me = forms.BooleanField(
        label='Keep me logged in',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )
    
    submit = forms.SubmitInput(attrs={'class': 'btn btn-primary', 'value': 'Log In'})
