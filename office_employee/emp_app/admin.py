from csv import list_dialects
from django.contrib import admin
from regex import R
from .models import Employee, Role, Department
# Register your models here.

class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']

class DepartmentAdmin(admin.ModelAdmin):
    class Meta:
        model = Department
        skip_unchanged = True
        report_skipped = True
        exclude = ('id', )
    list_display = ('name', 'location')

class EmpAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'dept', 'salary', 'bonus', 'role','phone', 'hire_date')


admin.site.register(Employee, EmpAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Department, DepartmentAdmin)