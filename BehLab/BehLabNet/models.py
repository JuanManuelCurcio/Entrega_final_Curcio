from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proyects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_proyect = models.CharField(max_length=500, null=False)
    brief_description = models.CharField(max_length=1250, null=False)
    key_words = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.name_proyect