from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from api.models import Voter, Candidate
from api.serializers import VoterSerializer, CandidateSerializer
from django.contrib.auth import authenticate, login
from django.http import JsonResponse



class VoterViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)

    return JsonResponse({'message': 'Invalid request method'}, status=405)