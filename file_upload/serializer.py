from rest_framework.serializers import Serializer, FileField, ModelSerializer

from .models import File

# # Serializers define the API representation.
# class UploadSerializer(Serializer):
#     file_uploaded = FileField()
#     class Meta:
#         fields = ['file_uploaded']


class UploadSerializer(ModelSerializer):
        class Meta:
            model = File
            fields = ('__all__') 