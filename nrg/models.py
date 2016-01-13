from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Questions(models.Model):
    vragen = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.vragen

