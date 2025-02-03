from django.db import models

# Create your models here.
class Receipt(models.Model):
    retailer = models.CharField()
    purchase_date = models.CharField()
    purchase_time = models.CharField()
    items = models.array
    total = models.FloatField()
    id = models.CharField() #str(uuid.uuid4()) #new uuid/endpoint
    points = models.IntegerField(default=None)

class Item(models.Model):
    short_description = models.CharField(max_length=200)
    price = models.FloatField()