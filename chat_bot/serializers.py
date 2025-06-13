from rest_framework import serializers
from .models import ChatMessage, ChatBot



class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = "__all__"

class ChatBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatBot
        fields = "__all__"
        read_only_fields = ['user', 'unique_id', 'count_messages', 'created_at', 'updated_at']