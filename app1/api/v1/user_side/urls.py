from django.urls import path,include
from rest_framework import routers
from app1.api.v1.user_side.views import *

# router = routers.DefaultRouter()

# router.register('blogs', BlogsView, basename='blogs')

# urlpatterns = router.urls

urlpatterns = [
    # path('router/', include(router.urls)),

    # ROLE
    path('role/', Roles.as_view(), name='role'),
    path('add/role/', AddRoles.as_view(), name='add_role'),
    
    # PRODUCTS
    path('product/vendor/', VendorProductsView.as_view(), name='vender_products'),
    path('product/customer/', CustomerProductsView.as_view(), name='customer_products'),


    # ADD PRODUCT TO CART
    path('product/cart/', CartProductsCountView.as_view(), name='cart_products'),
    path('product/customer/add/cart/', CustomerCartProductsView.as_view(), name='customer_cart_products'),


    # REGISTER USERS
    path('register/', Register.as_view(), name='register'),


]

