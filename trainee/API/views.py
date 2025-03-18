from rest_framework import status
from rest_framework.response import Response
#from rest_framework.viewsets import  ViewSet,ModelViewSet
from ..models import Trainee
from .serializers import Trainee_serializer
from rest_framework.views import APIView
from rest_framework import generics

class Trainee_List_Add(APIView): # listtrainee, add trainee--->API using class based view
    def get(self,req):
        return Response(
            data=Trainee_serializer.get_all_trainees_from_Ser(),
            status=status.HTTP_200_OK)
    def post(self,req):
        serobj=Trainee_serializer(data=req.data)
        if serobj.is_valid():
            serobj.save()
            return  Response(
                data=serobj.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data={'errors':serobj.errors}
            )
            
class Trainee_Update_Delete_Generic(generics.RetrieveUpdateDestroyAPIView): # update trainee, delete--->API using generice view

    queryset = Trainee.getAllTrainees()
    serializer_class = Trainee_serializer
    
    def destroy(self, request, *args, **kwargs):
        trainee_id = kwargs.get('pk')
        deleted = Trainee.deleteTraineeById(trainee_id)
        if deleted:  
            return Response({"message": "Trainee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": deleted.errors}, status=status.HTTP_400_BAD_REQUEST)