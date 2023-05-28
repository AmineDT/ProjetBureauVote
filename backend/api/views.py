from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from api.models import Voter, Candidate
from api.serializers import VoterSerializer, CandidateSerializer, VoterAuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response



class VoterViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
class VoterAuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        serializer = VoterAuthTokenSerializer(data={
            'token': token.key,
            'user_id': token.user_id
        })
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)