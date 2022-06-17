#from rest_framework_gis.filterset import GeoFilterSet
#from rest_framework_gis.filters import GeometryFilter
from rest_framework_gis.pagination import GeoJsonPagination
from .serializer import ServiceAreaSerializer
from .models import ServiceArea
from rest_framework import authentication, permissions, viewsets, filters, mixins
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from rest_framework import generics, status



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
        filters.OrderingFilter,
        #GeoFilterSet,
            )


class ServiceAreaList(DefaultsMixin, viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    pagination_class = GeoJsonPagination
    #print("queryset :",queryset)    
    @method_decorator(cache_page(60*2)) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



"""
class GetSpecificServiceArea(viewsets.ModelViewSet):
    
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('latitude','longitude')
    
    #@method_decorator(cache_page(60*2))
    def get_queryset(self):
        latitude = self.request.query_params.get('latitude',None)
        longitude = self.request.query_params.get('longitude', None)
        pnt = Point(float(latitude), float(longitude))
        qs = ServiceArea.objects.filter(geofence__contains=pnt)        
        return qs
"""


class GetSpecificServiceArea(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ServiceAreaSerializer
    filter_backends  = (DjangoFilterBackend,)
    #filterset_fields = ('lat', 'long')

    #@method_decorator(cache_page(60*2))
    def get_queryset(self):
        latitude = self.request.query_params.get('lat',None)
        longitude = self.request.query_params.get('long', None)
        pnt = Point(float(latitude), float(longitude))
        qs = ServiceArea.objects.filter(geofence__contains=pnt)        
        print(qs)
        return qs

    """ 
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ServiceAreaSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request):
        queryset = self.get_queryset()
        serializer =  ServiceAreaSerializer(queryset, many=True)
        #print(serializer.data)
        return Response(serializer.data)
    """
