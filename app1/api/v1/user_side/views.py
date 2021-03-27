from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from app1.api.v1.user_side.serializers import *
from app1.models import Products, CustomUsers, Cart, Role
from ecommerce.permissions import IsVender, IsCustomer

# CUSTOMER
class Roles(APIView):
    permission_classes = [AllowAny]
    def get(self, request):        
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True)
        return Response(serializer.data)


class AddRoles(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def post(self, request, format=None):
        res = request.data
        serializer = RoleSerializer(data=res)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# REGISTER
# CUSTOMER AND VENDOR
class Register(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request):
        response = request.data
        new_serializer = RegisterSerializer(data = response)

        data = {} 
        if new_serializer.is_valid():
            new_users = new_serializer.save()
            data['status'] = status.HTTP_201_CREATED
            data['response'] = 'Register successfully'
            # data['email'] = new_users.email
            # data['first_name'] = new_users.first_name
            # data['last_name'] = new_users.last_name
        else:
            data = new_serializer.errors
        return Response(data)


# End REGISTER



# VENDER PRODUCTS
class VendorProductsView(APIView):
    permission_classes = [IsAuthenticated, IsVender]

    def get(self, request):
        instance = request.user
        serializer = ProductsByVendorSerializer(instance)
        return Response(serializer.data)

    def post(self, request, format=None):
        res = request.data
        res['vendor'] = request.user.id
        serializer = ProductsSerializer(data=res)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# END VENDER PRODUCTS


# CUSTOMER CART PRODUCTS
class CustomerCartProductsView(APIView):
    permission_classes = [IsAuthenticated, IsCustomer]

    def get(self, request):        
        instance = request.user
        serializer = CartSerializer(instance)
        return Response(serializer.data)

    def post(self, request, format=None):
        res = request.data
        mutable = request.POST._mutable
        request.POST._mutable = True
        res["customer"] = request.user.id

        serializer = CartSerializer(data=res)

        if serializer.is_valid():
            serializer.save()
            request.POST._mutable = mutable
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# END CUSTOMER CART PRODUCTS


# CUSTOMER PRODUCTS
class CustomerProductsView(APIView):
    permission_classes = [IsAuthenticated, IsCustomer]

    def get(self, request):
        queryset = Products.objects.all()
        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# END CUSTOMER PRODUCTS


# CUSTOMER PRODUCTS
class CartProductsCountView(APIView):
    permission_classes = [IsAuthenticated, IsCustomer]

    def get(self, request):
        instance = request.user
        serializer = CartProductsByCustomerSerializer(instance)
        return Response(serializer.data)
# END CUSTOMER PRODUCTS