from django.urls import path
from login.views import login_user, submit_login, logout_user
from register import views
from register.api.viewsets import RegisterView

urlpatterns = [
    path('', views.register, name='register'),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),

    path('api/auth/', RegisterView.as_view(), name='register-endpoint'),

    # Endpoints
]
