from django.contrib import admin
from .models import StudentData,ProfessorData,StatusData,UniversityData,studentStatus
# Register your models here.
admin.site.register(StudentData)
admin.site.register(ProfessorData)
admin.site.register(UniversityData)
admin.site.register(StatusData)
admin.site.register(studentStatus)