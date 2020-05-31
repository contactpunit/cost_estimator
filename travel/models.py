from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Travel(models.Model):
    """Travel model deals with fields related to travel app"""
    country = models.CharField(max_length=60)
    source = models.CharField(max_length=60)
    destination = models.CharField(max_length=60)
    travel_date = models.DateField()
    num_passengers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Travel details - From {self.source} To {self.destination} DateOfTravel {self.travel_date}'
