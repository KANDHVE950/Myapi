from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import requests 
from django.core import serializers
from .serializers import DataSerializer
from .models import Data

from .forms import SignUpForm


def home(request):
	return render(request, 'index.html')

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			if User.objects.filter(username=form.cleaned_data.get('username')).exists():
				messages.info(request,'username already taken')
			else:
				user = form.save()
				login(request, user, backend='django.contrib.auth.backends.ModelBackend')
				return redirect('/')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})

def user_login(request):
	if request.method == 'POST':
		username = (request.POST['username'])
		password = (request.POST['password'])
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			print('user logged in')
			return redirect('/')
		else:
			messages.info(request, 'Invalid Credentials')
			return redirect('/login')
	else:
		return render(request, 'login.html')

def logout_view(request):
	logout(request)
	return redirect('/')


class DataView(CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = DataSerializer
	queryset = Data.objects.all()

	def get(self, request):
		queryset = self.get_queryset()
		serializer = DataSerializer(queryset, many=True)
		# content = {'message': 'Hello, World!'}
		return Response(serializer.data)

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		status_code = status.HTTP_201_CREATED
		response = {
			'success' : 'True',
			'status code' : status_code,
			'message': 'Data Updated  successfully',
			}

		return Response(response, status=status_code)


