from django.db import models


# Create your models here.
class Travel(models.Model):
    source = models.TextField()
    destination = models.TextField()
    country = models.TextField()
    travel_date = models.DateField(auto_now=True)
    num_travellers = models.IntegerField()

    def __str__(self):
        return f'Travel details - From {self.source} To {self.destination} DateOfTravel {self.travel_date} ' \
               f'NumPassengers {self.num_travellers} '
