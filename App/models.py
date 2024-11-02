from django.db import models
from .bot import chat
import re

# Create your models here.

class MessageBot(models.Model):
    user_input = models.TextField("User Message ")
    bot_response = models.TextField("Bot Answer", blank=True)

    def save(self, *args, **kwargs):
        if not self.bot_response:
            input_limpio = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s]', '', self.user_input)  
            self.bot_response = chat.get_response(input_limpio.strip().lower()).text
        super().save(*args, **kwargs)

    def __str__(self):
        return f"User: {self.user_input} | Bot: {self.bot_response}"