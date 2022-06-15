from django.urls import path
from login.views import login_user, submit_login, logout_user

urlpatterns = [
    path('', login_user),
    path('submit/', submit_login, name='submit'),
]
