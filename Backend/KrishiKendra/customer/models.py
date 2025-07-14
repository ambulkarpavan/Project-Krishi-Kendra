from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True)
    balance_due = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
