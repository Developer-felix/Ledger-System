"""
Auther : Onjomba Felix
Github Link : github.com/developer-felix
Country : Kenya
Year of Experience : 3 years
Working Place : Freelancer
Email : onjombafelix1@gmail.com
"""

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Account
from .serializers import WalletSerializer
from rest_framework import generics

#import all functions from logic.py
from .logic import *

#create post request for Create X amount to users one of the account.
@api_view(['POST'])
def create_x_amount_to_users(request):
    pass   