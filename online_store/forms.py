from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import UserProfile

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    phone = forms.CharField(max_length=15, required=False)
    address = forms.CharField(max_length=100, required=False)
    city = forms.CharField(max_length=50, required=False)
    country = forms.CharField(max_length=50, required=False)
    postal_code = forms.CharField(max_length=10, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',
                  'birth_date', 'phone', 'address', 'city', 'country', 'postal_code')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

            # Asignar grupo "Cliente"
            cliente_group, created = Group.objects.get_or_create(name="Cliente")
            user.groups.add(cliente_group)

            # Crear perfil
            UserProfile.objects.create(
                user=user,
                birth_date=self.cleaned_data['birth_date'],
                phone=self.cleaned_data['phone'],
                address=self.cleaned_data['address'],
                city=self.cleaned_data['city'],
                country=self.cleaned_data['country'],
                postal_code=self.cleaned_data['postal_code'],
            )

        return user