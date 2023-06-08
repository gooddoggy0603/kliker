from django.urls import path
from . import views

boost = views.BoostViewSet.as_view({
    'get': 'list',
    'post': 'create',
})


urlpatterns = [
    path('call_click/', views.call_click),
    path('boost/', boost, name='boosts'),
]
