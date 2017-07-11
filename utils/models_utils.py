from django.contrib.gis.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
