from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Grade(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='grades')
    grade = models.FloatField(
        validators=[
            MinValueValidator(0.0),  
            MaxValueValidator(100.0)  
        ]
    )

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}: {self.grade}"