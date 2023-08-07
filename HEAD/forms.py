from django import forms
from django.forms import ModelForm
from HEAD.apps.students.models import StudentData,studentStatus
from django.contrib.auth.models import User, Group

#Create a student form
class UpdateForm(ModelForm):
    class Meta:
        model = StudentData
        fields = ['name', 'university','date','status']

class UpdateStatusForm(ModelForm):
    class Meta:
        model = studentStatus
        fields = ['university','date','status']


class AddNewUserForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)
    
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'group']
