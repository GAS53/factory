from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", RedirectView.as_view(url="authorization/")),
    path('authorization/', include('authorization.urls', namespace='authorization')),
    path('technologist/', include('technologist.urls', namespace='technologist')),
]
