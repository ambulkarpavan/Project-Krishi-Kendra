from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('pesticide', 'Pesticide'),
        ('fungicide', 'Fungicide'),
        ('herbicide', 'Herbicide'),
        ('fertilizer', 'Fertilizer'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    unit = models.CharField(max_length=50)  # Litre, Kg, Pcs
    stock_qty = models.FloatField(default=0.0)
    purchase_price = models.FloatField()
    selling_price = models.FloatField()
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
