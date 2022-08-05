from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def home (request):
    pass