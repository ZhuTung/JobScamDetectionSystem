from django.db import models

# Create your models here.

class UserAccount(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.BigIntegerField(default=0)
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username