from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','fatherName','age','dob','rollNumber','address','phone','email','password','image')
