from rest_framework.serializers import Serializer, FileField, ModelSerializer

from .models import File

class UploadSerializer(ModelSerializer):
        class Meta:
            model = File
            fields = ('__all__') 