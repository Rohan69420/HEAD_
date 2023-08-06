from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class ProfessorData(models.Model):
    name = models.CharField(max_length=24, null=True)

    def __str__(self):
        return self.name


class UniversityData(models.Model):
    name = models.CharField(max_length=24, null=True)

    def __str__(self):
        return self.name


class StatusData(models.Model):
    name = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.name


class StudentData(models.Model):
    name = models.CharField(max_length=64, unique=True)
    university = models.ForeignKey(
        UniversityData, on_delete=models.SET_NULL, blank=True, null=True
    )
    professor = models.ForeignKey(
        ProfessorData, on_delete=models.SET_NULL, blank=True, null=True
    )
    age = models.IntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(1)], blank=True
    )
    date = models.DateField(blank=True, null=True)
    status = models.ForeignKey(
        StatusData, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.name
    
class studentStatus(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    university = models.ForeignKey(
        UniversityData, on_delete=models.SET_NULL, blank=True, null=True
    )
    professor = models.ForeignKey(
        ProfessorData, on_delete=models.SET_NULL, blank=True, null=True
    )
    age = models.IntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(1)], blank=True
    )
    date = models.DateField(blank=True, null=True)
    status = models.ForeignKey(
        StatusData, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.student.username