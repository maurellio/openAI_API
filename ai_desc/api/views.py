from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.views import View
from rest_framework.response import Response
from .utils import get_description, get_translation
from .models import Decriptions, Users

class TestView(APIView):
    def post(self, request):
        print('POST')
        print(request.data)
        return Response({'email': request.data}, status=status.HTTP_201_CREATED)

    def get(self, request):
        print('GET')
        print(request.data)
        return Response({'email': request.data}, status=status.HTTP_201_CREATED)

class CreateUser(APIView):
    def post(self, request):
        try:
            email = request.data['email']
        except:
            return Response({'ERROR': 'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)

        if not Users.objects.get(email=email):
            Users.objects.create(email=email)
            return Response({'email' : email}, status=status.HTTP_201_CREATED)
        else:
            return Response({'Error': 'User already exist'}, status=status.HTTP_400_BAD_REQUEST)



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
            return Response({'ERROR': 'SERVER SIDE ERROR'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'description': description_ru})
        # return Response(get_description(50, 'generate random text'))

