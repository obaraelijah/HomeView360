import uuid

from django.db import models


#used as a base class for other models. Any model that inherits from TimeStampedUUIDModel will automatically inherit its fields and functionality, including the auto-generated primary key and unique UUID
class TimeStampedUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True