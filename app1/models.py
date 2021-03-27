from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _

from django.db.models.signals import pre_save, post_save
from django.db import models
from ecommerce.utils import unique_slug_generator


# To create slug url
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
# End create slug url


# CUSTOM USER CREATE
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

    # Get student and teacher list
    def user(self):
        return self.filter(role='user').order_by('-id')

    def vendor(self):
        return self.filter(role = 'vendor').order_by('-id')


class CustomUsers(AbstractBaseUser, PermissionsMixin):
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)

    role = models.ForeignKey("Role", on_delete=models.CASCADE, null=True, related_name='roles')
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=250, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)


pre_save.connect(pre_save_receiver, sender=CustomUsers)
# END CUSTOM USER CREATE


# ROLE
class Role(models.Model):
    role = models.TextField(unique = True)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return str(self.role)

pre_save.connect(pre_save_receiver, sender=Role)
# END ROLE

# PRODUCTS
class Products(models.Model):
    vendor = models.ForeignKey(CustomUsers, on_delete=models.CASCADE, related_name='vendor_product')
    name = models.TextField()
    price = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='image/icon')
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return str(self.name)


pre_save.connect(pre_save_receiver, sender=Products)
# END PRODUCTS

# CART
class Cart(models.Model):
    customer = models.ForeignKey(CustomUsers, on_delete=models.CASCADE, related_name='customer_cart_product')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='products_in_cart')
# END CART


