from multiprocessing.managers import Token
from rest_framework import generics
from foodano import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login


class CategoryListCreateView(generics.ListCreateAPIView):
    serializers_class = serializers.CategoryListSerializer
    queryset = models.Category.objects.all()


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializers_class = serializers.CategoryDetailSerializer
    queryset = models.Category.objects.all()


# ===================================================================
class ProductListCreateView(generics.ListCreateAPIView):
    serializers_class = serializers.ProductListSerializer
    queryset = models.Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializers_class = serializers.ProductDetailSerializer
    queryset = models.Product.objects.all()


@api_view(['GET'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user  = authenticate(username=username, password=password)
    if user is not None:
        token_key, _ = Token.objects.get_or_create(user=user)
        context = {
            'success':True,
            'username': user.username,
            'key':token_key.key
        }
    else:
        context = {
            'success':False
        }

        return Response(context)