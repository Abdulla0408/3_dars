from django.urls import path
from . import views


urlpatterns = [
    path('category/create/list/', views.CategoryListCreateView.as_view()),
    path('category/detail/<int:id>/', views.ProductDetailView.as_view()),
    path('product/create/list/', views.ProductListCreateView.as_view()),
    path('product/detail/<int:id>/', views.ProductDetailView.as_view()),
    path('log-in', views.login),
]