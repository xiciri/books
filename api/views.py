from django.shortcuts import render
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,)

from bookapp.models import *
from .serializers import *


class BooksApiView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializerClass


class BooksDeteilView(RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializerClass

class BooksCreateView(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializerClass
    parser_classes = [MultiPartParser,FormParser]