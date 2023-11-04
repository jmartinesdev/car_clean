from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='clients/')),
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),
]