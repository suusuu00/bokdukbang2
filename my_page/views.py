from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MyInterest
from .serializers import MyInterestSerializer
from rooms_posts.models import Rooms
from rooms_posts.serializers import RoomsSerializer

# Create your views here.
class MyInterestList(APIView):
    def get(self, request):
        user = request.GET.get('user')

        interests = MyInterest.objects.filter(muser=user)
        serializer = MyInterestSerializer(interests, many=True)
        '''
        rooms_list = []
        for interest in interests:
            studio_id = interest.studio
            room = Rooms.objects.get(rooms_id=studio_id)
            rooms_list.append(room)

        RoomsSerializer(rooms_list, many=True)'''

        return Response(serializer.data)
    