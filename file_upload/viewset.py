import json

from .models import File
from .serializer import UploadSerializer

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


@permission_classes([IsAuthenticated])
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        print("KASDFLSAFDL")
        data = File.objects.filter(user_id = request.user)
        serializer_data = UploadSerializer(data, many=True)
        return Response(serializer_data.data)

    def create(self, request):
        file_uploaded = request.data['file']
       
        serializer_class = UploadSerializer(data = {"file":file_uploaded, 'data_uploaded': False, "user": request.user.id})

        if serializer_class.is_valid(raise_exception=True):
            try:
                if json.load(file_uploaded):
                    upload = File(file=file_uploaded, data_uploaded= False, user=request.user)
                    upload.save()
                    return Response(serializer_class.data, status=status.HTTP_200_OK)
            except:
                message = "JSON format only"

        else:
            message = "Something went wrong"

            
        return Response(message, status=status.HTTP_406_NOT_ACCEPTABLE)
