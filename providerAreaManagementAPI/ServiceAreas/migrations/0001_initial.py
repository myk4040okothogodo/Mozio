# Generated by Django 3.2.13 on 2022-06-16 20:04

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('geofence', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serviceArea_provider', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'serviceareas',
                'ordering': ['name'],
            },
        ),
    ]
