from django.db import models

class Car(models.Model):
	"""This class represents the car model."""
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	model = models.CharField(max_length=255, blank=False, unique=False)
	make = models.CharField(max_length=255, blank=False, unique=False)
	year = models.CharField(max_length=4, blank=False, unique=False)
	variant = models.CharField(max_length=255, blank=False, unique=False)
	image = models.TextField(blank=True, unique=False)

	def __str__(self):
		"""Return a human readable representation of the car model instance."""
		return "{}".format(self.name)