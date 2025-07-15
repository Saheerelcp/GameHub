from django.urls import path
from gamehubapp.views import homepage,registerpage,dashboard,registerpagepost,loginpost

urlpatterns = [
    path('home',homepage),
    path('register',registerpage),
    path('dashboard',dashboard),
    path('registerpagepost',registerpagepost),
    path('loginpost',loginpost)
]