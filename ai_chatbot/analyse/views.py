from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework import status
from .serializers import analyseserializer
from .document import extract_text_from_pdf
from .ai import analyse_document

class analyseAPI(APIView):
    def post(self,request):
        new_analyse=analyseserializer(data=request.data)

        if new_analyse.is_valid():
            document_file=request.FILES.get("document")
            queries=request.data.get("queries")

            document_text=extract_text_from_pdf(document_file)
            ai_result=analyse_document(
                document_text,
                queries
            )
            new_analyse.save()
            
            return Response(
                {
                    "ai_analysis":ai_result
                },
                status=status.HTTP_201_CREATED
                )
        return Response(
            new_analyse.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        