from django.contrib.gis.db import models as gis_models
from django.db import models
from django.conf import settings
import uuid



class ServiceArea(models.Model):
    """ An area that is served by a mozio Provider."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="serviceArea_provider", null=True, blank=True, on_delete=models.CASCADE)
    name  = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    geofence = gis_models.PolygonField()

    class Meta:
        db_table = "serviceareas"
        ordering = ['name']

    def __str__(self):
        return self.name


