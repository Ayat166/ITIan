from django.urls import path ,include
from .views import *

urlpatterns=[
    path('',traineeListGeneric.as_view(), name='traineeList'),
    path('addTrainee',traineeViewCreate.as_view(),name="addTrainee"),
    path('updateTrainee/<int:id>',traineeViewUpdate.as_view(),name="updateTrainee"),
    path('traineeDetails/<int:pk>',traineeListViewGeneric.as_view(),name="traineeDetails"),
    path('deleteTrainee/<int:pk>',traineeListDeleteGeneric.as_view(),name="deleteTrainee"),

]