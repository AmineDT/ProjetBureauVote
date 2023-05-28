from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response


class Voter(AbstractUser):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    public_key = models.CharField(max_length=255)
    voted = models.BooleanField(default=False)  # To mark if the voter has already voted
    groups = models.ManyToManyField(Group, related_name='voters', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='voters', blank=True)

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    vote_count = models.IntegerField(default=0)

class VoterAuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id})