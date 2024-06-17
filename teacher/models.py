from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    teacher_id = models.ImageField()
    email = models.EmailField()
    subject_specialization = models.CharField(max_length = 25)
    years_of_expperience = models.IntegerField()
    biography = models.TextField()

    def __str__(self):
            return f"{self.first_name} {self.last_name}"

    


