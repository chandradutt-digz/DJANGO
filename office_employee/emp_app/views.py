from ast import Return
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from regex import E
from emp_app.forms import EmployeeForm
from .models import Employee, Department, Role
from datetime import datetime
from django.db.models import Q
from django.contrib import messages
from office_employee.forms import EmployeeForm
# Create your views here.

def index(request):
    return render(request, 'index.html')


def allemp(request):
    emps = Employee.objects.all()
    data = {
        'emps': emps,
    }
    return render(request, 'allemp.html', data)


def addemp(request):
    item = Department.objects.all()
    roles = Role.objects.all()
    print('iiiiiiiiittttttttt', item)
    form = request.POST
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        print('rrrrrrrrrrrrrrrrrrr',request.POST.get('salary'))
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        dept = request.POST.get('dept')
        # dept = get_object_or_404(item, pk=request.POST.get('dept'))
        salary = int(request.POST.get('salary'))
        bonus = int(request.POST.get('bonus'))
        role = int(request.POST.get('role'))
        phone = int(request.POST.get('phone'))

        newemp = Employee(fname=fname, lname=lname,dept_id=dept, salary=salary, bonus=bonus, role_id=role, phone=phone, hire_date=datetime.now())
        newemp.save()
        return HttpResponse("employee added")
    elif request.method == 'GET':
        form = EmployeeForm()
        return render(request, 'addemp.html', {'item':item, 'role':roles,'form':form})
    else:
        return HttpResponse('An Error occurred Employee not Added')


def removeemp(request, emp_id = 0):
    if emp_id:
        try:
            emptoremove = Employee.objects.get(id=emp_id)
            emptoremove.delete()
            return HttpResponse('Employee Removed Successfully')
        except:
            return HttpResponse('Employee not Removed')
    emps = Employee.objects.all()
    context = {
        'emps': emps,
    }
    return render(request, 'removeemp.html', context)


def filteremp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        # lname = request.POST.get('lname')
        dept = (request.POST.get('dept'))
        role = request.POST.get('role')
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(fname__icontains = name) | Q(lname__icontains = name))
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name = role)
        
        context = {
            'emps': emps,
        }
        print(emps)
        return render(request, 'allemp.html', context)

    elif request.method == 'GET':
        return render(request, 'filteremp.html')
    else:
        return HttpResponse('An error occurred while processing')
    
def updateemp(request, id):
    emp = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=emp)
    if form.is_valid():
        form.save()
        return redirect('/allemp')
    return render(request, 'editemp.html', {'emp':emp})

def editemp(request, id):
    item = Department.objects.all()
    roles = Role.objects.all()
    employee = Employee.objects.get(id=id)
    return render(request, 'editemp.html', {'item': item, 'roles': roles, 'employee': employee})