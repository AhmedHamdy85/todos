from django.urls import path
from .views import TaskView,task_complet
urlpatterns = [
    path('tasks/', TaskView.as_view(), name='task-list'),
    path('tasks/create/', TaskView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskView.as_view(), name='task-detail'),
    path('tasks/update/<int:pk>/', TaskView.as_view(), name='task-update'),
    path('tasks/delete/<int:pk>/', TaskView.as_view(), name='task-delete'),
    path('tasks/switch/<int:pk>/', task_complet, name='task-switch'),
]