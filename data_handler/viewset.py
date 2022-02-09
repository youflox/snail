import json

from file_upload.models import File

from .models import Data
from .serializer import DataSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes



@permission_classes([IsAuthenticated])
class DataViewset(APIView):
    def post(self, request, format=None):
        file_id = request.data['file_id']
        queryset = Data.objects.filter(user = request.user).filter(file = file_id)
        serializer_data = DataSerializer(queryset, many=True)
        return Response(serializer_data.data)
  

# @commit_on_success
@permission_classes([IsAuthenticated])
class DataUploadViewset(APIView):
        def get(self, request, id=None):

            if id:
                user_id = request.user.id

                queryset = Data.objects.filter(file=id, user = user_id)

                serializer = DataSerializer(queryset, many=True)

                return Response(serializer.data,status=status.HTTP_200_OK)
                
            return Response(status=status.HTTP_200_OK)


        def post(self, request, format=None, id=None):

            if id:
                return Response("Please check URL for POST.", status=status.HTTP_400_BAD_REQUEST)


            file_id = request.data['file_id']
            user_id = request.user.id

            queryset = File.objects.filter(id=file_id).filter(user=user_id).get()
            json_data = json.load(queryset.file)
            print("HERE")
            try:
                for data in json_data:
                    data['file'] = file_id
                    data['user'] = request.user.id
                    serializer = DataSerializer(data = data)
                    if serializer.is_valid():
                        obj = Data.objects.create(
                            file_id = data['file'],
                            user_id = data['user'],
                            userId = data['userId'],
                            title = data["title"],
                            body = data["body"]
                        )
                        obj.save()

                queryset.data_uploaded = True
                queryset.save()

                return Response(status=status.HTTP_201_CREATED)
            except:
                return Response("File is not supported.", status=status.HTTP_406_NOT_ACCEPTABLE)
                    


{
"file_id":1
}
