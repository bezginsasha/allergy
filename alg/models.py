from django.db import models
from django.db import IntegrityError

# Create your models here.

class Allergy(models.Model):
	name = models.CharField(max_length=100, unique=True)
	anger = models.IntegerField(default=0)

	def save_with_unique_handle(self):
		if len(self.name) < 1:
			return

		try:
			self.save()
		except IntegrityError as e:
			pass

	@staticmethod
	def save_list(alg_list):
		for alg in alg_list:
			new_alg = Allergy(name = alg['name'], anger = alg['anger'])
			new_alg.save_with_unique_handle()

	def __str__(self):
		return "allergy " + self.name + " with anger: " + str(self.anger)