"""Django Serializer class with fields that correspond to the Model fields
   important to display data from the API to a form of data we can understand, like JSON or XML."""

from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
	"""Serializer to map the car model instance into JSON format."""

	class Meta:
		"""Serializer a model and their fields."""
		model = Car
		fields = ('id', 'model', 'manufacturer', 'year', 'variant', 'image', 'date_created', 'date_modified')
		read_only_fields = ('date_created', 'date_modified')
