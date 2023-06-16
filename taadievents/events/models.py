
# Create your models here.
from django.db import models
import uuid
# Create your models here.
class Customers(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    
class Event(models.Model):
    customer_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    picture_links = models.CharField(max_length=100)
    customer_id = models.ForeignKey(Customers,on_delete= models.CASCADE)