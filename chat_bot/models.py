from django.db import models
from accounts.models import CustomUser  # Assuming you have a User model in accounts app
# Create your models here.

class ChatBot(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='chat_bots')
    name = models.CharField(max_length=100, unique=True)
    style = models.CharField(max_length=50, choices=[
        ('modern', 'Modern'),
        ('classic', 'Classic'),
        ('minimal', 'Minimal'),
    ],
    null=True,
    blank=True
    )

    image = models.ImageField(upload_to='chat_bots_images/', blank=True, null=True)
    csv_file = models.FileField(upload_to='chat_bots_csv/', blank=True, null=True)
    website_link = models.URLField(blank=True, null=True)
    # unique_id = models.UUIDField(default=models.UUIDField().default, editable=False, unique=True)
    unique_id = models.UUIDField(default=models.UUIDField().default,  blank=True, null=True)
    count_messages = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

