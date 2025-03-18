from rest_framework import serializers
from ..models import Course

class Course_Serializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=255)
    status = serializers.BooleanField(default=True)
    
    def update(self, instance, validated_data):
        instance.name=validated_data['name']
        instance.save()
        return instance
    
    @classmethod
    def getupdatedCourse(cls,id,data):
        oldobj= Course.getCourseById(id)
        return Course_Serializer(instance=oldobj,data=data)


class CourseSerializerModel(serializers.ModelSerializer):  # Course---->API using View sets
    class Meta:
        model = Course
        fields = '__all__'