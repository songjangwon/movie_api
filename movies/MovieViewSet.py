from .models import Movie
from django.shortcuts import get_object_or_404
from myapps.serializers import MovieSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class MovieViewSet(viewsets.ViewSet):
    """
    A simple ViewSet that for listing or retrieving users.
    """

    def list(self, request):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = MovieSerializer(user)
        return Response(serializer.data)
