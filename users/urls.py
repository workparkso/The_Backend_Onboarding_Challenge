from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "users"

urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("refresh", TokenRefreshView.as_view(), name="refresh"),
]
