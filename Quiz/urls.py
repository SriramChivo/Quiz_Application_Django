from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from Quiz.views import login_auth_implementation
# from views import Auth_Implementation


urlpatterns = [
    # path('login/', TemplateView.as_view(template_name="home.html"),name="login"),
    path('register/', TemplateView.as_view(template_name="register.html"),name="register"),
    
    path('', login_auth_implementation.as_view(),name="auth-implementation"),
]
