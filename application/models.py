from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Travel(models.Model):

    CHOICES = [
    ('pending', 'pending'),
    ('approved', 'approved'),
    ('rejected', 'rejected'),
    ]

    trip = models.CharField(max_length=30, db_index=True, unique=True)
    traveldate = models.DateField(max_length=30)
    status = models.CharField( max_length=8, choices=CHOICES, default='pending')
    staff = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"Travel to {self.trip} on {self.traveldate}. Approved: {self.status}")
