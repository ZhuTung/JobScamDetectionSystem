from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    com_profile = models.CharField(max_length=500, null=True)
    desc = models.CharField(max_length=500, null=True)
    req = models.CharField(max_length=500, null=True)
    benefits = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.job_name