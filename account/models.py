from django.db import models

# Create your models here.
class User:
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=16)
    roll = models.IntegerField()

    class Meta:
        db_table = 'user'