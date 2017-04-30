from django.db import models, __all__
from django.forms import ModelForm
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=16)
    role = models.IntegerField()
    createtime = models.DateTimeField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'user'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password', 'role', 'createtime', 'updatetime']
