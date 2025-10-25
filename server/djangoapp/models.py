from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.name


class CarModel(models.Model):
    CAR_TYPE_CHOICES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('TRUCK', 'Truck'),
        ('VAN', 'Van'),
    ]
    
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)
    year = models.IntegerField(
        validators=[MinValueValidator(2015), MaxValueValidator(2023)]
    )
    created_at = models.DateTimeField(default=now)
    
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"


class CarDealer(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    lat = models.FloatField()
    long = models.FloatField()
    short_name = models.CharField(max_length=100)
    st = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.full_name} - {self.city}, {self.st}"


class DealerReview(models.Model):
    dealership = models.IntegerField()
    name = models.CharField(max_length=100)
    purchase = models.BooleanField()
    purchase_date = models.DateField()
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_year = models.IntegerField()
    sentiment = models.CharField(max_length=100)
    review = models.TextField()
    
    def __str__(self):
        return f"Review by {self.name} for {self.car_year} {self.car_make} {self.car_model}"