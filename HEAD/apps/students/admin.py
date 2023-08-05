from django.contrib import admin
from .models import StudentData,ProfessorData,StatusData,UniversityData,User
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username',) # add fields as you want

admin.site.register(User, CustomUserAdmin)
admin.site.register(StudentData)
admin.site.register(ProfessorData)
admin.site.register(UniversityData)
admin.site.register(StatusData)