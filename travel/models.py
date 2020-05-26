from django.db import models

# Create your models here.

class Travel(models.Model):
    source = models.TextField()
    destination = models.TextField()
    country = models.TextField()
    travel_date = models.DateField()
    num_passengers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Travel details - From {self.source} To {self.destination} DateOfTravel {self.travel_date}'
