from django.urls import include, path
from rest_framework import routers
from api.views import VoterViewSet, CandidateViewSet
from .views import VoterAuthTokenView

router = routers.DefaultRouter()
router.register('users', VoterViewSet)
router.register('candidates', CandidateViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', VoterAuthTokenView.as_view(), name='voter_auth_token'),
]
