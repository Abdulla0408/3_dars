from multiprocessing.managers import Token
from rest_framework import generics
from foodano import models
from . import serializers
from rest_framework.decorators import api_view, authentication_classes, permission_classes  
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.serializers import User
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required 


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
    

@api_view(['POST'])
def register(request):
    serializer = serializers.UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=204)

# =================================================================



class ProductCreateView(APIView):
    def post(self, request):
        serializer = serializers.ProductDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def product_delete(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class AddToCartView(APIView):
    @login_required 
    def post(self, request, product_id):
        product = get_object_or_404(models.Product, id=product_id)
        cart, _ = models.Cart.objects.get_or_create(author=request.user, is_active=True)
        product_img = product.images.first()
        cart_product, _ = models.CartProduct.objects.get_or_create(
            productImg=product_img,
            product=product,
            cart=cart
        )
        cart_product.quantity += 1
        cart_product.total_price = cart_product.quantity * product.price
        cart_product.save()
        return Response(status=status.HTTP_200_OK)

