from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blogger/', include('blogger.urls')),
    path('admin/', admin.site.urls),
]
