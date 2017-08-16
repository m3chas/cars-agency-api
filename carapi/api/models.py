from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=False)


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=False)


class Model(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, null=True)
    brand = models.ForeignKey(Brand, null=True)
    name = models.CharField(max_length=255, blank=False, unique=False)


class Car(models.Model):
    """This class represents the car model."""
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    manufacturer = models.ForeignKey(Manufacturer, null=True)
    brand = models.ForeignKey(Brand, null=True)
    model = models.ForeignKey(Model, null=True)
    year = models.DateField(blank=False)
    trim = models.CharField(max_length=255, blank=False, unique=False)
    image = models.TextField(blank=True, unique=False)

    def __str__(self):
        """Return a human readable representation of the car model instance."""
        return "{}".format(self.name)
