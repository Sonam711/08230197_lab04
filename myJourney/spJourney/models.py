from django.db import models

# Create your models here.
class LearningJourney(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    skills = models.TextField()
    hobbies = models.TextField()
    profile_image = models.ImageField(upload_to='profiles/',
blank= True,  null=True,)

    def __str__(self):
        return self.name
    

