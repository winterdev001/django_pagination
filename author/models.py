from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=150)
        
    def __str__(self):
        return f"Id: {self.id}, name: {self.name}"