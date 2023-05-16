from django.urls import include, path
from rest_framework import routers
from api.views import UserViewSet, CandidateViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('candidates', CandidateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
