from django.template.context_processors import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from course.models import Course
from .serializers import Course_Serializer ,CourseSerializerModel
from rest_framework.viewsets import ModelViewSet

@api_view(['PATCH'])
def update_Course(request,id):   #course update----> API using function based
    jsondaa=request.data
    courseSerialize=Course_Serializer.getupdatedCourse(id,jsondaa)
    if courseSerialize.is_valid() :
            courseSerialize.save()
            return Response(
                data=courseSerialize.data,
                status=status.HTTP_200_OK
            )
    else:
        return Response(
                {"error": courseSerialize.errors},
                status=status.HTTP_400_BAD_REQUEST)
        
        

class CourseViewSet(ModelViewSet): # Course---->API using View sets
    queryset = Course.getAllCourses()
    serializer_class = CourseSerializerModel
