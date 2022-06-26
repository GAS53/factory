from django.urls import path
from .views import RegisterView, IndexView, ProfileEditView, CustomLoginView, CustomLogoutView


app_name = 'authorization'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("login", CustomLoginView.as_view(), name="login"),
    path("logout", CustomLogoutView.as_view(), name="logout"),
    path("register", RegisterView.as_view(), name="register"),
    path("edit_profile", ProfileEditView.as_view(), name="edit_profile"),
    # path('register', RegisterView.as_view(),  name='register'),
]
