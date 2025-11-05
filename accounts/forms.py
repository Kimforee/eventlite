from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=Profile.ROLE_CHOICES,
        widget=forms.RadioSelect,
        required=True,
        help_text="Choose your role"
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Create or update profile with selected role
            profile, created = Profile.objects.get_or_create(user=user, defaults={'role': self.cleaned_data['role']})
            if not created:
                # Profile already exists (maybe from signal), update the role
                profile.role = self.cleaned_data['role']
                profile.save()
        return user

