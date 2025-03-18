from django.urls import path ,include
from .views import *
from .API.views import Trainee_List_Add,Trainee_Update_Delete_Generic
urlpatterns=[
    path('',traineeListGeneric.as_view(), name='traineeList'),
    path('addTrainee',traineeViewCreate.as_view(),name="addTrainee"),
    path('updateTrainee/<int:id>',traineeViewUpdate.as_view(),name="updateTrainee"),
    path('traineeDetails/<int:pk>',traineeListViewGeneric.as_view(),name="traineeDetails"),
    path('deleteTrainee/<int:pk>',traineeListDeleteGeneric.as_view(),name="deleteTrainee"),
    path('API',Trainee_List_Add.as_view()), #listtrainee, add trainee--->API using class based view
    path('API/<int:pk>',Trainee_Update_Delete_Generic.as_view()),
]