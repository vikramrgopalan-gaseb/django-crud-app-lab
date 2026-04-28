from django.db import models
from django.urls import reverse

CONDITION = (
    ('DS', 'Deadstock'),
    ('NDS', 'Near Deadstock'),
    ('W', 'Worn'),
)

class Condition(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('condition-detail', kwargs={'pk': self.id})

# Create your models here.
class Sneaker(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    colorway = models.TextField(max_length=250)
    year = models.IntegerField()
    condition = models.ManyToManyField(Condition)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('sneaker-detail', kwargs={'sneaker_id': self.id})
    
class Collection(models.Model):
    date = models.DateField("Collection Date")
    meal = models.CharField(max_length=1, choices=CONDITION, default=CONDITION[0][0])

    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_collection_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']