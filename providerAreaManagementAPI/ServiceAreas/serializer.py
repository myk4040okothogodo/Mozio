from rest_framework import serializers
from .models import ServiceArea
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model

Provider = get_user_model()

class ServiceAreaSerializer(serializers.ModelSerializer):
    provider = serializers.SlugRelatedField(slug_field = Provider.USERNAME_FIELD, queryset=Provider.objects.all(), required=False)
        
    links = serializers.SerializerMethodField('get_links')
    class Meta:
        model = ServiceArea
        fields = ('id','provider','name','price','geofence','links')


    def get_links(self, obj):
        request = self.context['request']
        links = { 'self': reverse('servicearea-detail', kwargs={'pk': obj.pk}, request=request),
                'provider': None,
                }

        if obj.provider_id:
            links['provider'] = reverse('provider-detail', kwargs={Provider.USERNAME_FIELD: obj.provider_id}, request=request)
        return links

