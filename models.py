from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SignUpForDailyDeals(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    signUp_date = models.DateField(auto_now_add=True)
