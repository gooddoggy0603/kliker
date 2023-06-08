from django.urls import path
from backend import views as bv

urlpatterns = [
    path('call_click/', bv.call_click),
]