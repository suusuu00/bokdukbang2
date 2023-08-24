from .models import Rooms
from rest_framework import serializers
from my_page.serializers import MyInterestSerializer
from chat.serializers import MessagesSerializer

class RoomsSerializer(serializers.ModelSerializer):

    studio_id = MyInterestSerializer(many=True, read_only=True)
    chatroom_id = MessagesSerializer(many=True, read_only=True)

    class Meta:
        model = Rooms
        fields = [
            "rooms_id",
            "ruser",
            "address",
            "area",
            "deposit",
            "monthly_rent",
            "maintenance_cost",
            "type",
            "start_date",
            "end_date",
            "structure",
            "women_only",
            "location",
            "sold",
            "category",
            "title",
            "comment",
            "interest",
            "date",
            "studio_id",
            "chatroom_id"
        ]