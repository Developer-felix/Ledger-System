"""
Auther : Onjomba Felix
Github Link : github.com/developer-felix
Country : Kenya
Year of Experience : 3 years
Working Place : Freelancer
Email : onjombafelix1@gmail.com
"""

from django.shortcuts import render
from .serializers import UserSerializer
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User


@api_view(['GET', 'POST'])
def user(request):
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = UserSerializer(data=data)


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

    elif request.method == 'GET':

        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response({'users': serializer.data,
                         'status': 'success',
                         'message': 'Users retrieved successfully'
                         }, status=status.HTTP_200_OK) 
