from django.db import models
from customer.models import Customer

class LedgerEntry(models.Model):
    TRANSACTION_TYPES = [
        ('sale', 'Sale'),
        ('payment', 'Payment Received'),
        ('adjustment', 'Adjustment'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    reference_id = models.CharField(max_length=100, blank=True)  # can store Sale.id or Payment id
    amount = models.FloatField()  # +ve for debit (customer owes), -ve for credit (customer paid)

    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.customer.name} - {self.transaction_type} - {self.amount}"
