from secrets import choice
from unicodedata import name
from django.db import models
from django.forms import CharField


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.name
    

class Employee(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, default='Free')
    salary = models.IntegerField()
    bonus = models.IntegerField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField()
    hire_date = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s %s %s %s %s %s %s %s" %(self.fname, self.lname, self.dept, self.salary, self.bonus, self.role, self.phone, self.hire_date)
    
    