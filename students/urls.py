from django.urls import path
from . import views
from .views import student_list, add_student, student_detail, student_delete


app_name = 'students'


urlpatterns = [
    path('list/', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('detail/<int:pk>/', views.student_detail, name='student_detail'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
]



