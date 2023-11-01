from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)  
    description = models.TextField() 
    instructor = models.CharField(max_length=255)  
    start_date = models.DateField()  # Date field for the course start date
    end_date = models.DateField()  # Date field for the course end date
    capacity = models.PositiveIntegerField()  

    def __str__(self):
        return self.title
