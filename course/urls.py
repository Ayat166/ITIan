from django.urls import path ,include
from .views import *
from .API.views import *
from rest_framework.routers import DefaultRouter
# Course---->API using View sets
router = DefaultRouter()
router.register(r'APIcourses', CourseViewSet) 

urlpatterns=[
    path('',courseList, name='courseList'),
    path('',include(router.urls)),  # Course---->API using View sets
    path('addCourse',addCourse,name="addCourse"),
    path('updateCourse/<int:id>',updateCourse,name="updateCourse"),
    path('deleteCourse/<int:id>',deleteCourse,name="deleteCourse"),
    path('API/<int:id>',update_Course)
]