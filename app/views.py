from django.shortcuts import render
from .models import Person
# Create your views here.

def selected_names(request):
    selected_names = Person.objects.values('name')
    return render(request, 'selected_names.html', {'selected_names': selected_names})

def excluded_people(request):
    excluded_people = Person.objects.exclude(age=30)
    return render(request, 'excluded_people.html', {'excluded_people': excluded_people})