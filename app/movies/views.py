from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Movie
from .serializers import MovieSerializer
from django.db import OperationalError

class MoviesList(APIView):
    def post(self, request, format=None):
        try:
            serializer = MovieSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except OperationalError:
                return Response({"error": "Database is not available make sure migrations have been executed."}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

    def get(self, request, format=None):
        try:
            movies = Movie.objects.all()
            print('Movies object: ', movies)
            # what if database is empty or no migrations have been run?
            if not movies:
                return Response({"message": "No movies found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)
        except OperationalError:
            return Response({"error": "Database is not available make sure migrations have been executed."}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

class MovieDetails(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
