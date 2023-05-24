from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Add any additional fields or modify existing fields as per your requirements
    # For example, you might want to add fields like full name, address, etc.
    # You can also remove or modify the existing fields from AbstractUser
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='api_users',
        related_query_name='api_user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='api_users',
        related_query_name='api_user_permissions'
    )

    def __str__(self):
        return self.username

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name