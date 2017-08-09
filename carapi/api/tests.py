# This quick project, has been done via Test-Driven Development (TDD).
# Code without tests is broken as designed. — Jacob Kaplan-Moss.

from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import Car

class ModelTestCase(TestCase):
    """Defines our test suite for the car model."""
	
    def setUp(self):
        """Define test client and test variables."""
		self.car_model = "Celica"
		self.car = Car(model=self.car_model)

	def test_model_can_create_a_car(self):
        """Test the car model can create a car."""
		latest_count = Car.objects.count()
		self.car.save()
		new_count  = Car.objects.count()
		self.assertNotEqual(latest_count, new_count)

    def test_model_returns_readable_data(self):
        """Test a readable string is returned for the car model instance."""
        self.assertEqual(str(self.car), self.name)

class ViewTestCase(TestCase):
    """Test Suite for API views."""

    def setUp(self):
        """Define test client and test variables."""
        self.client = APIClient()
        self.car_data = {'model': 'Celica', 'make': 'Toyota', 'year': '1986', 'variant':'Coupe', 'image':''}
        self.response = self.client.post(
            reverse('create'),
            self.car_data,
            format="json")

    def test_api_can_create_a_car(self):
        """Test the API can create a Car instance."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_car(self):
        """Test API can GET a given car."""
        car = Car.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': car.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, car)

    def test_api_can_update_a_car(self):
        """Test API can UPDATE a given car."""
        update_car = {'variant': 'Coupe Sport'}
        res = self.client.put(
            reverse('details', kwargs={'pk': car.id}),
            update_car, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_car(self):
        """Test API can DELETE a given car."""
        car = Car.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': car.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
