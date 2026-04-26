from django.db import models
from django.urls import reverse

CONDITION = (
    ('D', 'Deadstock'),
    ('NDS', 'Near Deadstock'),
    ('W', 'Worn'),
)

# Create your models here.
class Sneaker(models.Model):
    band = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    colorway = models.TextField(max_length=250)
    releasedate = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('sneaker-detail', kwargs={'sneaker_id': self.id})
    
class Condition(models.Model):
    condition = models.CharField(max_length=1, choices=CONDITION, default=CONDITION[0][0])

    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

class Sneaker:
    def __init__(self, brand, model, colorway, releasedate):
        self.brand = brand
        self.model = model
        self.colorway = colorway
        self.resleasedate = releasedate

sneakers = [
    Sneaker('Nike', 'Huarache', 'Scream Green', 1991),
    Sneaker('Air Jordan', 'VII', 'Playoff', 1992),
    Sneaker('Reebok', 'Pump', 'White', 1989),
    Sneaker('Adidas', 'Crazy 8', 'Purple', 1997),
]