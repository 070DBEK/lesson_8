from django.urls import path
from . import views
from students.urls import app_name


app_name = 'teachers'


urlpatterns=[
    path('list/', views.teacher_list, name='teacher_list'),
    path('add/', views.add_teacher, name='add_teacher'),
    path('detail/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('delete/<int:pk>/', views.teacher_delete, name='teacher_delete'),
]