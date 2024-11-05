# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    CABRIO = "Cabrio"
    SPORT = "Sport"
    CAR_TYPE_CHOICES = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon"),
        (CABRIO, "Cabrio"),
        (SPORT, "Sport"),
    ]
    car_type = models.CharField(
        max_length=7,
        choices=CAR_TYPE_CHOICES,
        default=SEDAN,
    )
    year = models.IntegerField(
        default=2024, validators=[MinValueValidator(2015), MaxValueValidator(2023)]
    )

    def __str__(self):
        return self.name