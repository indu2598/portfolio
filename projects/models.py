from django.db import models

# Create your models here.
class ProjectInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    github = models.URLField()
    demo = models.URLField(blank=True)
    image = models.ImageField(upload_to="photos/", blank = True)
    show = models.BooleanField(default=False)

def __str__(self):
    return self.name
