from django.db import models

# Create your models here.
class jobseekerapp(models.Model):
    name=models.CharField(max_length=120)
    qualification=models.CharField(max_length=120)
    hobbies=models.TextField()
    skills=models.TextField()
    address=models.TextField()
    profile_photo=models.ImageField(upload_to='profile_photo/')
def __str__(self):
    return self.name