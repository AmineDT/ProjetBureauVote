from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from api.models import User, Candidate
from api.serializers import UserSerializer, CandidateSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
