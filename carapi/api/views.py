from django.shortcuts import render
from rest_framework import generics
from django_filters import rest_framework as filters
from dateutil.relativedelta import relativedelta
import datetime
from .serializers import CarSerializer
from .models import Car


class AgeFilter(filters.NumberFilter):
	"""Custom filter on a date based on the age entered as input"""

	def filter(self, qs, value):
		if value is not None:
			now = datetime.date.today()
			age_req = str(value).partition('.')  # Split the user input as srt.
			month_req = int(age_req[2]) if age_req[2] else 0
			get_date = (now + relativedelta(years=-(int(age_req[0])), months=-month_req))
			if month_req > 0:
				return qs.filter(year__year=get_date.year, year__month=get_date.month)
			else:
				return qs.filter(year__year=get_date.year)
		return qs


class CarFilter(filters.FilterSet):
	"""Custom FilterSet to include our custom filters and filter fields"""

	age = AgeFilter(name='year')  # Custom filter based on age.

	class Meta:
		model = Car
		fields = ['make', 'model', 'age']


class CreateView(generics.ListCreateAPIView):
	"""This class handles the GET and POST methods requests on our API."""

	queryset = Car.objects.all()
	serializer_class = CarSerializer
	filter_class = CarFilter

	def perform_create(self, serializer):
		serializer.save()  # Save a new car instance from our POST request.


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""This class handles GET, PUT, PATCH and DELETE requests on our API"""

	queryset = Car.objects.all()
	serializer_class = CarSerializer
