from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my/',include('myapp.urls')),
    path('my1/',include('myapp1.urls')),
]
