from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Bills(models.Model):
    name = models.CharField(max_length=200)
    xid = models.CharField(max_length=200)
    description = models.TextField()
    update_date = models.DateField()
    created_date = models.DateField()

    def __str__(self):
        return self.name


class RegistrationVoteUser(models.Model):
    user_id = models.ForeignKey(User)
    street_address = models.CharField(max_length=200)
    street_address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    home_phone = models.CharField(max_length=200)

    def __str__(self):
        return self.home_phone
