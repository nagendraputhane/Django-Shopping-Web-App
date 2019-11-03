from django.db import models

# Create your models here.
class Locality(models.Model):
    city = models.CharField(max_length=64)

    def __str__(self):
        return '%s' %(self.city)

class Shop(models.Model):
    area = models.ForeignKey(Locality, on_delete=models.CASCADE, related_name="location")
    name = models.CharField(max_length=64)

    def __str__(self):
        return '%s  [Location: %s]' %(self.name, self.area)

class Item(models.Model):
    itemname = models.CharField(max_length=64)
    shops = models.ManyToManyField(Shop, blank=True, related_name="items")

    def __str__(self):
        return "%s" %(self.itemname)

class CartItems(models.Model):
    content = models.CharField(max_length=64)

    def __str__(self):
        return "%s" %(self.content)
