from django.db import models

class Greeting(models.Model):
    salutation = models.CharField(max_length=100)
    def __unicode__(self):
        return self.salutation

# Create your models here.
