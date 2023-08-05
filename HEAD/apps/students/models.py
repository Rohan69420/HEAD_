from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


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

#custom user model
class User(AbstractUser):
	"""
    Default custom user model for HEAD.
    """

	class Types(models.TextChoices):
		TEACHER = "TEACHER", "Teacher"
		STUDENT = "STUDENT", "Student"
		ADMIN = "ADMIN", "Admin"

	first_name = None  # type: ignore
	last_name = None  # type: ignore

	# Replacing the default from django of first and last name to have a
	# name value which encompasses all of them in single field
	name = models.CharField(_("Name of User"), blank=True, max_length=255)
	type = models.CharField(_("Type"), max_length=64, choices=Types.choices, default=Types.ADMIN)

	# Admins will create accounts, and in such case password will be generated automatically, hence
	# Initial password is used to store the automatically generated password
	#initial_password = models.CharField(max_length=10, null=True, blank=True)

	def __str__(self):
		return self.name