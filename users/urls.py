from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("signup", views.SignupView.as_view(), name="signup"),
    path("login", views.LoginView.as_view(), name="login"),
    path("refresh", views.CustomTokenRefreshView.as_view(), name="refresh"),
    path("protected", views.ProtectedView.as_view(), name="protected"),
]



# 기존에는 함수형인 views.~로 작성했으나,
# Django REST framework의 클래스형 뷰는 코드 재사용성과 유지보수 측면에서 유리하므로, 
# as_view() 방식으로 통일