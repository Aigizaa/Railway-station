
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.urls import path
from Railway.views import station

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Railway.urls')),
]
