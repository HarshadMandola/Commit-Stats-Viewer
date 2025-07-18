from django.db import models

# Create your models here.
class Commits(models.Model):
    created_dates=models.DateField()
    author_name=models.CharField( max_length=100)
    email=models.EmailField( max_length=254)
    project_name=models.CharField( max_length=100)
    hash_commit=models.CharField( max_length=50)
    merge=models.BooleanField("merger status")
    added_lines=models.IntegerField(default=0)
    deleted_lines=models.IntegerField(default=0)


    def __str__(self):
        return f"{self.author_name} - {self.email}"