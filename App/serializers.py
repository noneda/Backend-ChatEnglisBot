from rest_framework import serializers
from .models import MessageBot

class MessageBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageBot;
        fields = '__all__'