from django.contrib import admin

from .models import Address, Student

class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['name', 'lastname']}),
        ('Birthdate information',  {'fields': ['birthdate']}),
        ('Address information', {'fields': ['address']}),
    ]

admin.site.register(Student, StudentAdmin)
admin.site.register(Address)