from django.db import models


class Travel(models.Model):
    source = models.CharField(max_length=60)
    destination = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    travel_date = models.DateField()
    num_passengers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Travel details - From {self.source} To {self.destination} DateOfTravel {self.travel_date}'
