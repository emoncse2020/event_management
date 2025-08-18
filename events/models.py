from django.db import models

# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"

class Event(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return f"{self.name} | {self.date}"
    
class Participant(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True )
    events = models.ManyToManyField(Event, related_name='participants', blank=True)



    def __str__(self):
        return f"{self.name} | {self.email}"
    

   

