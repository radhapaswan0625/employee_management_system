from django.shortcuts import render
from employees.models import Employee

def home(request):
    employees = Employee.objects.all()
    return render(request, "home/index.html", {
        "employees": employees
    })