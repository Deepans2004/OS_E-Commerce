from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    age = forms.IntegerField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    dob = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    address = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name',
            'password1', 'password2'
        ]

    def save(self, commit=True):
        # Save the User instance first without committing to DB
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()  # Save user to DB first
            # Then create the related Profile instance
            Profile.objects.create(
                user=user,
                age=self.cleaned_data['age'],
                phone=self.cleaned_data['phone'],
                dob=self.cleaned_data['dob'],
                address=self.cleaned_data['address']
            )
        return user
