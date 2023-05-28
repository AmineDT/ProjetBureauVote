from django.urls import include, path
from rest_framework import routers
from api.views import VoterViewSet, CandidateViewSet, login_view

router = routers.DefaultRouter()
router.register('users', VoterViewSet)
router.register('candidates', CandidateViewSet)
path('auth/login/', login_view, name='login'),

urlpatterns = [
    path('', include(router.urls)),
]
