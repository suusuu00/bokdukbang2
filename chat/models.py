from django.db import models
from accounts.models import User
from rooms_posts.models import Rooms

# Create your models here.


class Messages(models.Model):
    messages_id = models.AutoField(primary_key=True)
    chatroom = models.ForeignKey(Rooms, on_delete=models.CASCADE, blank=False, null=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, db_column='sender', blank=False, null=False)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    isread = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'messages'
        
        
