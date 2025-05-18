from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create or update the Profile whenever
    a User instance is created or saved.
    """
    if created:
        # Create Profile for new User
        Profile.objects.create(user=instance, age=0, phone='', address='')
    else:
        # For existing user, just save profile to trigger any save logic
        instance.profile.save()
