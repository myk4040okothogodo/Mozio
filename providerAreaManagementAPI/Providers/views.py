from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets, filters
from .serializer import ProviderSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


Provider = get_user_model()


class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering and pagination."""
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
            )
    permission_classes = (
        permissions.IsAuthenticated,
        #TokenHasReadWriteScope,
        )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
            )



class ProviderViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing Providers."""
    lookup_field = Provider.USERNAME_FIELD
    lookup_url_kwarg = Provider.USERNAME_FIELD
    queryset = Provider.objects.order_by(Provider.USERNAME_FIELD)
    serializer_class = ProviderSerializer

    @method_decorator(cache_page(60*2))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

