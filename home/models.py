from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Travel(models.Model):
    destination = models.CharField(max_length=30, db_index=True, unique=True)
    traveldate = models.DateField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
