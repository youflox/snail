from django.urls import path, include
from rest_framework import routers

from .viewset import DataViewset, DataUploadViewset


urlpatterns = [
    path('', DataViewset.as_view()),
    path('upload/', DataUploadViewset.as_view()),
    path('upload/<int:id>', DataUploadViewset.as_view())
]