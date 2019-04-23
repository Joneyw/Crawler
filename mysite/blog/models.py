from django.db import models

# Create your models here.
class Movie(models.Model):
    id=models.BigIntegerField    
    name = models.CharField(max_length=255, blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    evaluate = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.id

class Weather(models.Model):
    city =models.CharField(max_length=255,blank=True,null=True)
    day=models.CharField(max_length=255,blank=True,null=True)
    weather=models.CharField(max_length=255,blank=True,null=True)
    temperature_high=models.CharField(max_length=255,blank=True,null=True)
    temperature_lower=models.CharField(max_length=255,blank=True,null=True)        

    def __str__(self):
        return self.id

class JD_goods(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)
    price=models.CharField(max_length=255,blank=True,null=True)
    comment=models.CharField(max_length=255,blank=True,null=True)
    link=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.id

