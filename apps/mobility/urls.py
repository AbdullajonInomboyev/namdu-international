from django.urls import path
from . import views
app_name = 'mobility'
urlpatterns = [
    path('', views.index, name='index'),
]
