from django.urls import path
from .views import TaskView
urlpatterns = [
    path('tasks/',TaskView.as_view()),
    path('tasks/create/',TaskView.as_view()),
    path('tasks/update/<int:pk>/',TaskView.as_view()),
    path('tasks/delete/<int:pk>/',TaskView.as_view()),
    path('tasks/<int:pk>/',TaskView.as_view()),
]
