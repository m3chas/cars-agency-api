# Cars Agency API

## Introduction

> Create a RESTful API service that will make CRUD operations possible on the collection of cars agency.

## Requirements

> PostgreSQL

> Python 3.x
> Django==1.11.4
> django-filter==1.0.4
> djangorestframework==3.6.3
> drfdocs==0.0.11
> psycopg2==2.7.3
> pytz==2017.2

## Business Logic

> Create: It should be possible to create new car objects via API
> Read: It should be possible to read existing car objects via API.
> Filter: There should be a way to filter out the objects by the make, model and the age of the car.
> Update: Support for updating the car object via API
> Delete: Deletion support of the car object

## URLs

> /api/docs/
> /api/cars/
> /api/cars/<ID>
> /api/cars?make=Toyota
> /api/cars?year=1986
> /api/cars?model=Celica
> /api/cars?make=Toyota&year=1986&model=Celica
