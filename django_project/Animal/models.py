from django.db import models

class Animal(models.Model):
	kingdom = models.CharField(max_length=100)
	family = models.CharField(max_length=100)
	specie = models.CharField(max_length=100)
	lifespan = models.IntegerField()

	def __str__(self):
		return f"{self.kingdom} {self.family} {self.specie} ({self.lifespan})"
