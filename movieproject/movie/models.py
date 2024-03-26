from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=10)
    director = models.CharField(max_length=20)
    lead_actor = models.CharField(max_length=20)
    lead_actress = models.CharField(max_length=20)
    ticket_fare = models.IntegerField()
    choice = [('Online', 'ONLINE'), ('Cash', 'Cash On Delivery')]
    payment_mode = models.CharField(max_length=10, choices=choice)

