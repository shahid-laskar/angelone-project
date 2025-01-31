from django.urls import path
from .views import login, callback

urlpatterns = [
    path('login/', login, name='login'),
    path('callback/', callback, name='callback'),
]
