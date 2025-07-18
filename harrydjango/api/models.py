from django.db import models

# Create your models here.
class Issues(models.Model):
    issue_id=models.CharField( max_length=50)
    issue_key=models.CharField( max_length=50)
    created_date=models.DateTimeField( )
    name=models.CharField(max_length=50)