from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

User = settings.AUTH_USER_MODEL
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
    name = models.CharField(max_length=12,blank=True,null=True)
    def __str__(self):
        return self.name

class StudentData(models.Model):
    # something like this should be added in models
    # but since we're adding to already existing data some default value needs to be given 
    # This is a nightmare lmao 
    # student = models.ForeignKey(
	# 	User,
	# 	on_delete=models.CASCADE,
	# 	related_name="my_requests",
	# 	related_query_name="my_requests"
	# )	
    name = models.CharField(max_length=64, unique=True)
    university = models.ForeignKey(UniversityData, on_delete=models.SET_NULL, null=True)
    professor = models.ForeignKey(ProfessorData,on_delete=models.SET_NULL,null=True)
    age = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)])
    date = models.DateField(blank=True, null=True)
    status = models.ForeignKey(StatusData,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name