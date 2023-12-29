from django.db import models

# Create your models here.

class TOPIC(models.Model):
    topic_name = models.CharField(max_length = 100,primary_key = True)
    
    def __str__(self) :
        return self.topic_name
    
class WEBPAGE(models.Model):
    topic_name = models.ForeignKey(TOPIC,on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    def __str__(self) :
        return self.name

class Accessrecord(models.Model):
    name = models.ForeignKey(WEBPAGE,on_delete=models.CASCADE)
    date = models.DateField()
    author = models.CharField(max_length=100)
    
    def __str__(self) :
        return self.author