from django.db import models
from django.contrib.auth.models import User

class TopUp(models.Model):
    """Model untuk top up CP"""
    cp_amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.cp_amount} CP - {self.price}"


class Transaction(models.Model):
    """Model untuk transaksi top up"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    top_up = models.ForeignKey(TopUp, on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.CharField(max_length=20, choices=(
        ("pending", "Pending"),
        ("success", "Success"),
        ("failed", "Failed"),
    ), default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.top_up.cp_amount} CP"