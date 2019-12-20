from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .serializers import TodoSerializer
from .models import Movie
from .models import Todo
from rest_framework.response import Response
from rest_framework.decorators import action
import sys
from PyQt5.QtWidgets import *

class MovieViewSet(viewsets.ModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer


	@action(detail=True, methods=['get'])
	def start_pystock(self, request, pk):
		print('ffdfasdfsdf')
		print('123465849')
		app = QApplication(sys.argv)
		label = QLabel("Hello PyQt")
		label.show()
		app.exec_()

class TodoViewSet(viewsets.ModelViewSet):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer

