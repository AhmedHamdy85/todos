from django.urls import path
from .views import *

urlpatterns = [
    path('regester/',UserRegesterView.as_view()),
    path('login/',CustomTokenObtainPairView.as_view()),
    path('',UserRegesterView.as_view()),
    path('<int:pk>',UserRegesterView.as_view()),
    path('logout/', LogoutView.as_view())
]
