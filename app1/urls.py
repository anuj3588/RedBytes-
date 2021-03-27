from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    # API
    path('api/v1/', include('app1.api.v1.user_side.urls')),
    
    # TEMPLATES
    path('', dashBoardView, name="login"),
    path('register/', register, name="register"),
    path('cart/', cart, name="cart"),
    path('login-submit/', loginSubmit, name="login_submit"),
    path('logout/', LogoutView, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
