from django import forms
from django.forms import ModelForm
from HEAD.apps.students.models import StudentData

#Create a student form
class UpdateForm(ModelForm):
    class Meta:
        model = StudentData
        fields = ['name', 'university','date','status']