from django.urls import path
from .views import RegisterView, IndexView, ProfileEditView, user_login, logout_view
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'authorization'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("login/", user_login, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("edit_profile/", ProfileEditView.as_view(), name="edit_profile"),
    # path('register', RegisterView.as_view(),  name='register'),
]
