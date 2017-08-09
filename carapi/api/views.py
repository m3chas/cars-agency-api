from django.shortcuts import render

# Views used by our Django App
from rest_framework import generics
from django_filters import rest_framework as filters
from .serializers import CarSerializer
from .models import Car

class CreateView(generics.ListCreateAPIView):
	"""This class handles the GET and POST methods requests on our API."""

	queryset = Car.objects.all()
	serializer_class = CarSerializer
	"""Fields used for filter objets"""
	filter_fields = ('make', 'model', 'year')

	def perform_create(self, serializer):
		"""Save POST data values when creating a new car."""

		serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""This class handles GET, PUT, PATCH and DELETE requests on our API"""

	queryset = Car.objects.all()
	serializer_class = CarSerializer