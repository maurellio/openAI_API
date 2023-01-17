from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.views import View
from rest_framework.response import Response
from .utils import get_description, get_translation
from .models import Decriptions, Users

class TestView(APIView):
    """
    Just a test method to see the data from web-hook
    """
    def post(self, request):
        print('POST')
        print(request.data)
        return Response({'email': request.data}, status=status.HTTP_201_CREATED)

    def get(self, request):
        print('GET')
        print(request.data)
        return Response({'email': request.data}, status=status.HTTP_201_CREATED)

class CreateUser(APIView):
    """
    Here is a method for creating a user. This method takes 'email'.
    """
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
    """
    Here is an API method which doing next stuff:
    1) Get the original response['text'] and the original language['language']
    2) Translate it to English
    3) Send request to open AI
    4) Translate response from openAI to original language
    """
    def post(self, request):
        try:
            email = request.data['email']
            desc_req_ru = request.data['text']
            language = request.data['language']
        except:
            return Response({'ERROR': 'some fields was not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Users.objects.get(email=email)
        except:
            return Response({'ERROR': 'User is not registered'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            desc_req_eng = get_translation(desc_req_ru, 'EN-US')
            description_eng = get_description(200, desc_req_eng)
            description_ru = get_translation(description_eng, language)
            description_ru_length = len(description_ru)

            user.tokens = description_ru_length + user.tokens
            user.save()

            Decriptions.objects.create(user_req=desc_req_ru, description_ru=description_ru, user=user)
        except Exception as e:
            Decriptions.objects.create(user_req=desc_req_ru, error=repr(e))
            return Response({'ERROR': 'SERVER SIDE ERROR'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'description': description_ru})
        # return Response(get_description(50, 'generate random text'))

