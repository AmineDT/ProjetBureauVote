from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from api.models import Voter, Candidate
from api.serializers import VoterSerializer, CandidateSerializer
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import views, status


class VoterViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class LoginView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Authentication successful'})
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)