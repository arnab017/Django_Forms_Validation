from django.db import models

# Create your models here.

class Student(models.Model):
    s_id = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=50)
    s_age = models.IntegerField()

    def __str__(self):
        return self.s_name