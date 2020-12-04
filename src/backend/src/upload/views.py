from .serializers import PostSerializer
from .models import Upload
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

# Create your views here.

class UploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        uploads = Upload.objects.all()
        serializer = PostSerializer(uploads, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        upload_serializer = PostSerializer(data=request.data)
        if upload_serializer.is_valid():
            upload_serializer.save()
            return Response(upload_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Error", upload_serializer.errors)
            return Response(upload_serializer.errors, status=status.HTTP_400_BAD_REQUEST)