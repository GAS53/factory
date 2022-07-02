from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import IndexView, H701View

app_name = 'technologist'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    # path("H701/", H701View.as_view(), name="H701"),
    path('H701/', H701View.as_view(),  name='H701'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)