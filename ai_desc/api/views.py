from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.views import View
from rest_framework.response import Response
from .utils import get_description, get_translation
from .models import Decriptions


class Generate(APIView):
    def post(self, request):
        try:
            desc_req_ru = request.data['text']
        except:
            return Response({'ERROR': '"text" field was not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            desc_req_eng = get_translation(desc_req_ru, 'EN-US')
            description_eng = get_description(200, desc_req_eng)
            description_ru = get_translation(description_eng, 'RU')
            Decriptions.objects.create(user_req=desc_req_ru, description_ru=description_ru)
        except Exception as e:
            Decriptions.objects.create(user_req=desc_req_ru, error=repr(e))
        return Response({'description': description_ru})
        # return Response(get_description(50, 'generate random text'))
