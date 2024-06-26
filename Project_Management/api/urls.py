from django.urls import path
from .views import *

urlpatterns = [
    path('users/register/', signup),
    path('users/login/', login),
    path('users/<int:id>/', user_detail),
    path('projects/', project_list),
    path('projects/<int:id>/', project_detail),
    path('projects/<int:id>/tasks/', task_list),
    path('tasks/<int:id>/', task_detail),
    path('tasks/<int:id>/comments/', comment_list),
    path('comments/<int:id>/', comment_detail),
]
