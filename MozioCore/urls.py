from django.conf.urls import include, url
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path
from providerAreaManagementAPI.urls import router
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    path('api/', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace="oauth2_provider")),
    url(r'openapi/', get_schema_view(
        title="MozioService",
        description ="An API to allow Client self-registration and Querying of various ServiceArea "
        ), name="openapi-schema"),
   url(r'docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]

