from django.db import models
from django.contrib.auth.models import User

class Investment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  stock_symbol = models.CharField(max_length=10)
  amount_invested = models.DecimalField(max_digits=10, decimal_places=2)
  date_invested = models.DateField()
  
class InvestmentHistory(models.Model):
  investment = models.ForeignKey(Investment, on_delete=models.CASCADE, related_name='history')
  date = models.DateField()
  value = models.DecimalField(max_digits=10, decimal_places=2)
  