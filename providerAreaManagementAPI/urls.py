from rest_framework.routers import DefaultRouter
from .Providers.views import  ProviderViewSet
from .ServiceAreas.views import ServiceAreaList
from .ServiceAreas.views import GetSpecificServiceArea

router = DefaultRouter()

router.register(r'providers' , ProviderViewSet)
router.register(r'serviceareas', ServiceAreaList)
router.register(r'getspecificarea', GetSpecificServiceArea, basename='GetSpecificArea')


#router.register(r'^getspecificarea', GetSpecificServiceArea, basename='GetSpecificArea')

