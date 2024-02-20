from django.urls import path,include
from myapp import views
from myapp.views import admiralView
urlpatterns = [
    path('abc/',views.fun1),
    path('one/<x>',views.fun2),
    path('two/',admiralView.as_view())
]