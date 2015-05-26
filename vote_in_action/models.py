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