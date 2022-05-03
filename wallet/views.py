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
    if request.method == "POST":
        data = request.data
        print(data)
        serializer = WalletSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'error': False,
                'error_message': '',
                'message': 'User created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'failed',
            'error': True,
            'error_message': '',
            'message': 'User not created',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

#Debit X amount from users one of the account.
@api_view(['POST'])
def debit_x_amount_from_users(request):
    if request.method == "POST":
        data = request.data
        print(data)
        serializer = WalletSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'error': False,
                'error_message': '',
                'message': 'User created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'failed',
            'error': True,
            'error_message': '',
            'message': 'User not created',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

#Transfer money from one account to another account for a single user.
@api_view(['POST'])
def transfer_money_from_one_account_to_another_account(request):
    if request.method == "POST":
        data = request.data
        print(data)
        serializer = WalletSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'error': False,
                'error_message': '',
                'message': 'User created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'failed',
            'error': True,
            'error_message': '',
            'message': 'User not created',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)  



#Transfer money from one account of user to another account of another user.
@api_view(['POST'])
def transfer_money_from_one_account_to_another_account_of_another_user(request):
    if request.method == "POST":
        data = request.data
        print(data)
        serializer = WalletSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'error': False,
                'error_message': '',
                'message': 'User created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'failed',
            'error': True,
            'error_message': '',
            'message': 'User not created',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# 
# 
#Get balance for a user.
@api_view(['GET'])
def get_balance_for_a_user(request):
    if request.method == "GET":
        data = request.data
        print(data)
        serializer = WalletSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'error': False,
                'error_message': '',
                'message': 'User created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'failed',
            'error': True,
            'error_message': '',
            'message': 'User not created',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# Get balance for an account of a user.
@api_view(['GET'])
def get_balance_for_an_account_of_a_user(request):
    if request.method == "GET":
        data = request.data
        print(data)
        serializer = WalletSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'error': False,
                'error_message': '',
                'message': 'User created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'failed',
            'error': True,
            'error_message': '',
            'message': 'User not created',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
