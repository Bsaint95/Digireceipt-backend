import json
import datetime
from rest_framework import viewsets, status
from django.shortcuts import render
from django.http import JsonResponse
from .models import customers
from .serializers import customersSerializer
from rest_framework.decorators import api_view

class indexViewSet(viewsets.ModelViewSet):
	queryset = customers.objects.all().order_by('name')
	serializer_class = customersSerializer

@api_view(['GET'])
def single(request, id):
	if request.method == 'GET':
		try:
			customer = customers.objects.get(id = id)
			return JsonResponse(customer, safe = False)
		except:
			return JsonResponse({
				'error': 'customer does not exist'
				}, status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def customer(request):
    if request.method == 'POST':
        issue_no = request.data['issue_no']
        name = request.data['name']
        email = request.data['email']
        platform = request.data['platform']
        return JsonResponse(issue_no, name, email, platform, safe = False)
		

