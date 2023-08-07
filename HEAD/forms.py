from django import forms
from django.forms import ModelForm
from HEAD.apps.students.models import StudentData,studentStatus

#Create a student form
class UpdateForm(ModelForm):
    class Meta:
        model = StudentData
        fields = ['name', 'university','date','status']

class UpdateStatusForm(ModelForm):
    class Meta:
        model = studentStatus
        fields = ['university','date','status']