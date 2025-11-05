from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a Profile when a new User is created"""
    if created:
        # Only create if profile doesn't exist in database (check properly)
        if not Profile.objects.filter(user=instance).exists():
            Profile.objects.create(user=instance, role='ATTENDEE')  # Default role

