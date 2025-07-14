from django.db import models
from customer.models import Customer
from inventory.models import Product

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()
    paid_amount = models.FloatField()
    balance_due = models.FloatField()

    def __str__(self):
        return f"Sale #{self.id} - {self.customer.name}"

class InvoiceItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    rate = models.FloatField()
    subtotal = models.FloatField()

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
