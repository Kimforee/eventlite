from django import forms
from .models import Event, Session

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'starts_at']
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(attrs={'rows': 5}),
            'starts_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['title', 'starts_at', 'ends_at']
        widgets = {
            'title': forms.TextInput(),
            'starts_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'ends_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

