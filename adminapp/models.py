from django.db import models


class useraccount(models.Model):
    ROLE_CHOICES = [
        ('employer', 'Employer'),
        ('jobseeker', 'Job Seeker'),
    ]
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    email = models.EmailField(primary_key=True)
    phonenumber = models.CharField(max_length=10)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.firstname

# Create your models here.