from django.db import models

class Friend(models.Model):
	image = models.ImageField(upload_to='images/')
	character = models.CharField(max_length=300)
	
# Create your models here.
