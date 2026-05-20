from django.urls import path
from . import views
app_name = 'partnerships'
urlpatterns = [
    path('', views.index, name='index'),
    path('mou/', views.mou_list, name='mou_list'),
    path('<int:pk>/', views.detail, name='detail'),
]
