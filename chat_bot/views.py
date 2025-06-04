from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_chatbot(request):
    if request.method == 'POST':
        try:
            user = request.user
            chatbot = ChatBotSerializer(data=request.data)
            if chatbot.is_valid():
                chatbot.save(user=user)
                return Response({"unique_id": chatbot.data['unique_id']}, status=status.HTTP_201_CREATED)
            else:
                return Response(chatbot.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@api_view(['POST'])
@permission_classes([])
def chatMessage(request):
    if request.method == 'POST':
        try:
            message = request.data.get('message')
            unique_id = request.data.get('unique_id')
        
            if not message or not unique_id:
                return Response({"error": "Message and unique_id are required"}, status=status.HTTP_400_BAD_REQUEST)

            chat_bot = ChatBot.objects.get(unique_id=unique_id)
            if not chat_bot:
                return Response({"error": "Chat bot not found"}, status=status.HTTP_404_NOT_FOUND)


            # condition to check if the subscription is active and message limit is not exceeded
            
            # Here you would typically call your AI model to get a response based on the message
            bot_response = " "

            # For demonstration, we will just echo the message back
            chat_bot.count_messages += 1
            chat_bot.save()
            return Response({"bot_response": bot_response}, status=status.HTTP_201_CREATED)
        
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

