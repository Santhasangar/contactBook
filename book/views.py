from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import contactBookSerializer
from .models import contactBook
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class contactBookList(generics.ListAPIView):
    queryset = contactBook.objects.all()
    serializer_class = contactBookSerializer
    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAuthenticated,]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['userName','email']
    pagination_class = PageNumberPagination

# Creating the new entries for contacts
class createContactAPIView(APIView):
    def get(self, request):
        Contact = contactBook.objects.all()
        serializer = contactBookSerializer(Contact, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = contactBookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# This view will be getting used to update the contact
class contactBookDetailView(APIView):
    def get_object(self, id):
        try:
            return contactBook.objects.get(id=id)
        except contactBook.DoesNotExist as e:
            return Response({"error" : "Given contact book detail not found."}, status=404)
            
    def get(self, request, id=None):
        instance = self.get_object(id)
        serializer = contactBookSerializer(instance)
        return Response(serializer.data)

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = contactBookSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, id=None):
        instance = self.get_object(id)
        instance.delete()
        return Response({'msg':"data deleted"}, status=204)



