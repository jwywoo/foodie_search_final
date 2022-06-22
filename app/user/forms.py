from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class SignupForm(forms.Form):
    username = forms.CharField(
        label='username',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        label='email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password2 = forms.CharField(
        label='password check',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise ValidationError("INVALIDE USERNAME")
        return data

    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            self.add_error('password2', 'password should match')
        return self.cleaned_data

    def signup(self):
        fields = [
            'username',
            'email',
            'password',
        ]
        create_user_dict = {}
        for key, value in self.cleaned_data.items():
            if key in fields:
                create_user_dict[key] = value

        create_user_dict = {key: value for key, value in self.cleaned_data.items() if key in fields}

        def in_fields(item):
            return item[0] in fields

        result = filter(in_fields, self.cleaned_data.items())
        create_user_dict = {}
        for item in result:
            create_user_dict[item[0]] = item[1]

        create_user_dict = dict(filter(in_fields, self.cleaned_data.items()))
        create_user_dict = dict(filter(lambda item: item[0] in fields, self.cleaned_data.items()))

        user = User.objects.create_user(**create_user_dict)
        return user

