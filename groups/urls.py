from django.urls import path
from . import views



app_name = 'groups'


urlpatterns=[
    path('list/', views.group_list, name='group_list'),
    path('add/', views.add_group, name='add_group'),
    path('detail/<int:pk>/', views.group_detail, name='group_detail'),
    path('delete/<int:pk>/', views.group_delete, name='group_delete'),
]