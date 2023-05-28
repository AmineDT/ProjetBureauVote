from django.urls import include, path
from rest_framework import routers
from api.views import VoterViewSet, CandidateViewSet, LoginView

router = routers.DefaultRouter()
router.register('users', VoterViewSet)
router.register('candidates', CandidateViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', LoginView.as_view(), name='login'),
]
