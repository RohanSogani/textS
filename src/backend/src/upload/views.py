from .serializers import PostSerializer
from .models import Upload
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
import os

# Create your views here.
BASE_DIR = "/home/ecs289gnlp/textS/"

class UploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        uploads = Upload.objects.all()
        serializer = PostSerializer(uploads, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        upload_serializer = PostSerializer(data=request.data)
        file_name = str(request.data['pdf'])
        if upload_serializer.is_valid():
            upload_serializer.save()
            pdf_file_path = BASE_DIR + "src/backend/src/media/post_pdfs/" + file_name

            cmd_convert_pdf = "python3 " + BASE_DIR + "src/backend/scripts/convertPDF.py " + pdf_file_path

            os.system(cmd_convert_pdf)

            file_name = file_name.split(".")
            file_name = file_name[0] + ".txt"
            txt_file_path = BASE_DIR + "src/backend/src/media/post_pdfs/" + file_name
            cmd = "sh " + BASE_DIR + "src/backend/scripts/run_pegasus.sh " + txt_file_path

            os.system(cmd)
            print(upload_serializer.data)
            return Response(upload_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Error", upload_serializer.errors)
            return Response(upload_serializer.errors, status=status.HTTP_400_BAD_REQUEST)