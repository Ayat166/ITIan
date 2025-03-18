from rest_framework import serializers
from ..models import Trainee

class Trainee_serializer(serializers.ModelSerializer):
    class Meta():
        model=Trainee
        fields='__all__'
        
    @classmethod
    def get_all_trainees_from_Ser(cls):
        return cls(Trainee.getAllTrainees(),many=True).data
    
    # @classmethod
    # def delete_trainee_from_Ser(cls,id):
    #     Trainee.deleteTraineeById(id)
    #     return True