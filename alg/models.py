from django.db import models

# Create your models here.

class Allergy(models.Model):
	name = models.CharField(max_length=100)
	anger = models.IntegerField(default=0)

	def __str__(self):
		return "allergy " + self.name + " with anger: " + str(self.anger)