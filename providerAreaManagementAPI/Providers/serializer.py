from django.contrib.auth import get_user_model 
from rest_framework import serializers
from .models import Provider,ProviderProfile
from rest_framework.reverse import reverse



Provider = get_user_model()


class ProviderSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    currency_display = serializers.SerializerMethodField('get_currency_display')
    language_display = serializers.SerializerMethodField('get_language_display')

    class Meta:
        model =  Provider
        fields =  ['id',Provider.USERNAME_FIELD,'first_name','last_name','language','language_display','currency','currency_display','links']

    def get_currency_display(self, obj):
        return obj.get_currency_display()

    def get_language_display(self, obj):
        return obj.get_language_display()
    
    def get_links(self, obj):
        request = self.context['request']
        username = obj.get_username()
        return {
                #'self': reverse('provider-detail',
                #kwargs = {Provider.USERNAME_FIELD: username}, request=request),
            'serviceareas':'{}?provider={}'.format(
                    reverse('servicearea-list', request=request), username) 
            }



    """
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        provider = Provider.objects.create(**validated_data)
        ProviderProfile.objects.create(provider=provider, **profile_data)
        return provider
           
    
    def update(self, instance, validated_data):
        #handle related objects
        for related_obj_name in self.Meta.related_fields:
            #Validated data will show the nested structure
            data = validated_data.pop(related_obj_name)

            #same as default update implementation
            for attr_name,value in data.items():
                setattr(related_instance, attr_name, value)
            related_instance.save()
        return
    """

