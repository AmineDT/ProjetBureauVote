from rest_framework import serializers
from api.models import Candidate, Voter
from rest_framework.authtoken.serializers import AuthTokenSerializer


class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = ['id', 'name', 'surname', 'date_of_birth', 'public_key', 'voted']

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'name', 'vote_count']

class VoterAuthTokenSerializer(AuthTokenSerializer):
    token = serializers.CharField()
    user_id = serializers.IntegerField()