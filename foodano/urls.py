from django.urls import path
from .views import (main, banner_list, banner_create, banner_detail, banner_update, banner_delete,
                    category_list, category_create, category_detail, category_update, category_delete,
                    product_list, product_create, product_detail, product_update, product_delete,
                    info_list, info_create, info_detail, info_update, info_delete,
                    product_enter_list, product_enter_create, product_enter_detail, product_enter_update, product_enter_delete,
                    wishlist, add_to_wishlist, remove_from_wishlist,
                    view_cart, update_cart_quantity, checkout, order_confirmation, add_to_cart, remove_from_cart,
                    register, user_login, user_logout
                    )


urlpatterns = [
    path('', main, name="main"),
    path('banner_list/', banner_list, name="banner_list"),
    path('banner_create/', banner_create, name="banner_create"),
    path('banner_detail/<int:pk>/', banner_detail, name="banner_detail"),
    path('banner_update/<int:pk>/', banner_update, name="banner_update"),
    path('banner_delete/<int:pk>/', banner_delete, name="banner_delete"),

    # ============================================================================

    path('category_list/', category_list, name="category_list"),
    path('category_detail/<int:pk>/', category_detail, name="category_detail"),
    path('category_create/', category_create, name="category_create"),
    path('category_update/<int:pk>/', category_update, name="category_update"),
    path('category_delete/<int:pk>/', category_delete, name="category_delete"),

    # ==================================================================================

    path('product_list/', product_list, name="product_list"),
    path('product_detail/<int:pk>/', product_detail, name="product_detail"),
    path('product_create/', product_create, name="product_create"),
    path('product_update/<int:pk>/', product_update, name="product_update"),
    path('product_delete/<int:pk>/', product_delete, name="product_delete"),

    # ==================================================================================

    path('info_list/', info_list, name="info_list"),
    path('info_create/', info_create, name="info_create"),
    path('info_detail/<int:pk>/', info_detail, name="info_detail"),
    path('info_update/<int:pk>/', info_update, name="info_update"),
    path('info_delete/<int:pk>/', info_delete, name="info_delete"),

    # ==================================================================================

    path('product_enter_list/', product_enter_list, name="product_enter_list"),
    path('product_enter_create/', product_enter_create, name="product_enter_create"),
    path('product_enter_detail/<int:pk>/', product_enter_detail, name="product_enter_detail"),
    path('product_enter_update/<int:pk>/', product_enter_update, name="product_enter_update"),
    path('product_enter_delete/<int:pk>/', product_enter_delete, name="product_enter_delete"),

    # ==================================================================================

    path('wishlist/', wishlist, name="wishlist"),
    path('add_to_wishlist/<int:product_id>/', add_to_wishlist, name="add_to_wishlist"),
    path('remove_from_wishlist/<int:product_id>/', remove_from_wishlist, name="remove_from_wishlist"),

    # ==================================================================================


    path('view_cart/', view_cart, name="view_cart"),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update_cart_quantity/<int:cart_product_id>/', update_cart_quantity, name="update_cart_quantity"),
    path('remove-from-cart/<int:cart_product_id>/', remove_from_cart, name="remove_from_cart"),
    path('checkout/', checkout, name="checkout"),
    path('order_confirmation/', order_confirmation, name="order_confirmation"),
    
    # ==================================================================================

    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
]