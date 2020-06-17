from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{}-{}".format(self.date, self.amount)

    pass


class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{}-{}".format(self.date, self.amount)
