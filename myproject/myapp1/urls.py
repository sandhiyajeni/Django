from django.urls import path,include
from myapp1 import views
urlpatterns = [
    path('c/',views.fun1)
]