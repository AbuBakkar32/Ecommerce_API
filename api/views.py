from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView

from api.models import *
from rest_framework import generics
from .serialiers import CategoriSerializer, BookSelializer, ProductSelializer


# Create your views here.
class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriSerializer


class ListCategory(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriSerializer


class DetailsCategory(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriSerializer


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSelializer


class ListBook(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSelializer


class DetailsBook(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSelializer


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSelializer


class ListProduct(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSelializer


class DetailsProduct(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSelializer


def index(request):
    return render(request, 'index.html')
