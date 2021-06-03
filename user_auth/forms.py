from django.contrib.auth.forms import UserCreationForm, ValidationError
from django import forms
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email address (optional)', required=False,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # check if email exists in database
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise ValidationError('Email address exists')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user
