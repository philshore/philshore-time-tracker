from django.db import models
from django.contrib.auth.models import User


# Set email field to unique
User._meta.get_field('email')._unique = True
# User Profile Model


class UserComponent(models.Model):
    """
    Contains user profile information.
    """
    user = models.OneToOneField(User, primary_key=True)
    component = models.CharField(max_length=100)
