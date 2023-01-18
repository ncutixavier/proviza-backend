from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.QuestionsList.as_view()),
    path('', views.QuestionCreate.as_view(), name='create-question'),
    path('<int:pk>/', views.QuestionUpdate.as_view(), name='update-question'),
    path('<int:pk>/', views.QuestionDelete.as_view(), name='delete-question')
]
