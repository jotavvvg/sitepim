from django.shortcuts import render
from django.http import HttpResponse
def home_view(request):
    return render(request, 'project.html')
def signup_view(request):
    return render(request, 'signup.html')

