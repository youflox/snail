from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User  

from rest_framework.decorators import api_view


def home(request):
    return HttpResponse('Working')

@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        from django.contrib.auth import authenticate, login

        user = authenticate(username='admin', password='admin')
        if user is not None:
            login(request, user)

        return HttpResponse(request.user)


    if request.method == 'GET':
        return HttpResponse('GET METHOD')

def logout(request):
    pass


def signup(request):
    pass
