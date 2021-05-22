from django.contrib.auth.forms import UserCreationForm, ValidationError
from django.contrib.auth.models import User
from django.forms import EmailField


class UserCreationForm(UserCreationForm):
    email = EmailField(label='email address', required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

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
