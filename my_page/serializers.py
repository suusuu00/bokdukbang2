from .models import MyInterest
from rest_framework import serializers

class MyInterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyInterest
        fields = "__all__"