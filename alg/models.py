from django.db import models

# Create your models here.

class Allergy(models.Model):
	name = models.CharField(max_length=100)
	anger = models.IntegerField(default=0)