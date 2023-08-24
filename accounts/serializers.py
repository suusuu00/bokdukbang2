from .models import User
from rest_framework import serializers
from rooms_posts.serializers import RoomsSerializer
from my_page.serializers import MyInterestSerializer
from chat.serializers import MessagesSerializer

class UserSerializer(serializers.ModelSerializer):
    ruser_id = RoomsSerializer(many=True, read_only=True)
    muser_id = MyInterestSerializer(many=True, read_only=True)
    sender_id = MessagesSerializer(many=True, read_only=True)


    class Meta:
        model = User
        fields = [
            "user_id",
            "username",
            "student_num"
            "email",
            "password",
            "created_at",
            "last_login",
            "phone",
            "ruser_id",
            "muser_id",
            "sender_id"
        ]