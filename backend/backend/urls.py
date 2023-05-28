from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/auth/token/', VoterAuthTokenView.as_view(), name='voter_auth_token'),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
