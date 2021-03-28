from rest_framework import serializers, status
from app1.models import *

# ROLE
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'role', 'slug']
        read_only_fields = ['slug']
# END ROLE

#  REGISTRATION
class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = CustomUsers
        fields = ["first_name", "last_name", "email", "password", "confirm_password", "phone_number", "role"]

        extra_kwargs = {
            'email' : {'required':True},
            'password' : {'write_only':True, 'required':True},
        }

    def save(self):
        print('self.validated_data'), self.validated_data['role']
        if self.is_valid():
            users = CustomUsers(
                first_name = self.validated_data['first_name'],
                last_name = self.validated_data['last_name'],
                email = self.validated_data['email'],
                phone_number =  self.validated_data['phone_number'],
                role =  self.validated_data['role'],

            )
            password = self.validated_data['password']
            confirm_password = self.validated_data['confirm_password']

            if password != confirm_password:
                raise serializers.ValidationError({'password':'Password must match', 'status':status.HTTP_400_BAD_REQUEST})
            users.set_password(password)
            users.save()

            return users
# END  REGISTRATION


# VENDER REGISTRATION
class VenderRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = CustomUsers
        fields = ["first_name", "last_name", "email", "password", "confirm_password", "phone_number"]

        extra_kwargs = {
            'email' : {'required':True},
            'password' : {'write_only':True, 'required':True},
        }

    def save(self):
        if self.is_valid():
            users = CustomUsers(
                first_name = self.validated_data['first_name'],
                last_name = self.validated_data['last_name'],
                email = self.validated_data['email'],
                phone_number =  self.validated_data['phone_number'],
                is_vendor = True,
            )
            
            password = self.validated_data['password']
            confirm_password = self.validated_data['confirm_password']

            if password != confirm_password:
                raise serializers.ValidationError({'password':'Password must match', 'status':status.HTTP_400_BAD_REQUEST})
            users.set_password(password)
            users.save()

            return users
# END VENDER REGISTRATION



# PRODUCTS
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'price', 'icon', 'vendor','slug']
        read_only_fields = ['slug']

class ProductsByVendorSerializer(serializers.ModelSerializer):
    vendor_product = ProductsSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUsers
        fields = ['first_name', 'last_name', 'email', 'slug', 'vendor_product']
        read_only_fields = ['slug']
# END PRODUCTS

# CART PRODUCTS
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
        read_only_fields = ['slug']

class CartProductsByCustomerSerializer(serializers.ModelSerializer):
    customer_cart_product = ProductsSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUsers
        fields = ['first_name', 'last_name', 'email', 'slug', 'customer_cart_product']
        read_only_fields = ['slug']
# END CART PRODUCTS


# CART PRODUCT COUINT OF USER
class CartProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','product']
        read_only_fields = ['slug']
        depth = 1

class CartProductsByCustomerSerializer(serializers.ModelSerializer):
    customer_cart_product = CartProductsSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUsers
        fields = ['first_name', 'last_name', 'email', 'slug', 'customer_cart_product']
        read_only_fields = ['slug']
# END CART PRODUCT COUINT OF USER