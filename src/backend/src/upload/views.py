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
        request.data['txt'] = ""
        file_name = str(request.data['pdf'])
        if upload_serializer.is_valid():
            upload_serializer.save()
            pdf_file_path = BASE_DIR + "src/backend/src/media/post_pdfs/" + file_name

            cmd = "sh " + BASE_DIR + "src/backend/scripts/run_pegasus.sh " + pdf_file_path

            os.system(cmd)
            copy_file = BASE_DIR + "src/pegasus/ckpt/pegasus_ckpt/arxiv/predictions-340000-.dev.txt"
            return_txt = ""
            with open(copy_file, 'r') as file:
                return_txt = file.read().replace('\n', '')
            # print(return_txt)
            request.data['txt'] = return_txt
            # print(upload_serializer.data)
            return Response(return_txt, status=status.HTTP_201_CREATED)
        else:
            print("Error", upload_serializer.errors)
            return Response(upload_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
