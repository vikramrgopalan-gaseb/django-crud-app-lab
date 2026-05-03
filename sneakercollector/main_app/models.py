from django.db import models
from django.urls import reverse

CONDITION_CHOICES = (
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

class Sneaker(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    colorway = models.TextField(max_length=250)
    year = models.IntegerField()
    
    conditions = models.ManyToManyField(Condition)

    def __str__(self):
        
        return f"{self.brand} {self.model}"
    
    def get_absolute_url(self):
        return reverse('sneaker-detail', kwargs={'sneaker_id': self.id})
    
class Collection(models.Model):
    date = models.DateField("Collection Date")
    
    condition = models.CharField(
        max_length=3, 
        choices=CONDITION_CHOICES, 
        default=CONDITION_CHOICES[0][0]
    )
    
    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']