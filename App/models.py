from django.db import models
from .Bot import chat

# Create your models here.

class MessageBot(models.Model):
    user_input = models.TextField("User Message ")
    bot_response = models.TextField("Bot Answer", blank=True)

    def save(self, *args, **kwargs):
        if not self.bot_response:
            self.bot_response = chat.get_response(self.user_input).text
        super().save(*args, **kwargs)

    def __str__(self):
        return f"User: {self.user_input} | Bot: {self.bot_response}"