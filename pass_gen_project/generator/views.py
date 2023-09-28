from django.http import HttpResponse
from django.shortcuts import render
import random as r


def home(request):
  return render(request, 'generator/home.html')


def password(request):
  thepassword = ''
  length = int(request.GET.get('length', 12))
  chars = 'abcdefghijklmnopqrstuvwxyz'

  if request.GET.get('uppercase'):
    chars += 'abcdefghijklmnopqrstuvwxyz'.upper()

  if request.GET.get('numbers'):
    chars += '1234567890'

  if request.GET.get('special'):
    chars += '“!@#$%^&*()_+=?><'

  for i in range(length):
    thepassword += r.choice(chars)

  return render(request, 'generator/password.html', {
    'password': thepassword
  })


def about(request):
  return render(request, 'generator/about.html')