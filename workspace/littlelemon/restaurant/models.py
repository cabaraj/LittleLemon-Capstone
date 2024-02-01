from django.db import models

# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    name = models.CharField(max_length=255)
    guests = models.SmallIntegerField()
    date = models.DateField()

    def __str__(self):
        return f'{self.name} ({self.guests})'