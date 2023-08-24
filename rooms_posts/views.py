#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rooms
from rooms_posts.serializers import RoomsSerializer
from rooms_posts.models import Rooms
from datetime import timedelta
from django.utils import timezone

# Create your views here.
class FindRoomsList(APIView):
    
    def get(self, request):
        id = request.GET.get('id')

        # 모든 방 구하기 글 최신순으로 정렬
        if id == "all":
            rooms = Rooms.objects.filter(category="방 구하기").order_by("-date")
            serializer = RoomsSerializer(rooms, many=True)

            return Response(serializer.data)
        
        # 특정 방 구하기 글
        elif id.isdigit():
            room = Rooms.objects.filter(pk=id, category="방 구하기")
            serializer = RoomsSerializer(room)

            return Response(serializer.data)

        # 특정 구에 있는 방 구하기 글 최신순으로 정렬
        else:
            id_values = id.split(',')

            rooms = Rooms.objects.filter(address__icontains=id_values[0], category="방 구하기")

            if len(id_values) != 1:  # id 값이 여러 개일 경우
                for i in id_values[1:]:
                    rooms = rooms | Rooms.objects.filter(address__icontains=i, category="방 구하기")

            sorted_rooms = sorted(rooms, key=lambda room: room.date, reverse=True)
            serializer = RoomsSerializer(sorted_rooms, many=True)

            return Response(serializer.data)

class FindRoomsAdd(APIView):
    def post(self, request):
        data = request.data  # 요청 데이터 추출 (실제 데이터 형식에 맞게 수정해야 합니다.)
        new_room = Rooms.objects.create(
            ruser = data.get('user'), # user_id
            type = data.get('type'), # 임대유형
            start_date = data.get('start_date'),
            end_date = data.get('end_date'),
            structure = data.get('structure'), # 방 구조
            women_only = data.get('women_only'),
            location = data.get('location'), # 희망 위치
            category = data.get('category'), # 방 구하기
            title = data.get('title'),
            comment = data.get('comment'),
            interest = data.get('interest'),
        )
        serialized_room = RoomsSerializer(new_room).data
        return Response({'message': 'Room added successfully', 'room': serialized_room})

class FindRoomsPut(APIView):
    # 특정 구하기 글 수정
    def put(self, request):
        id = request.GET.get('id')

        try:
            room = Rooms.objects.get(id=id)
        except Rooms.DoesNotExist:
            return Response({"message": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = RoomsSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FindRoomsDelete(APIView):
    # 특정 구하기 글 삭제
    def delete(self, request):
        id = request.GET.get('id')

        try:
            room = Rooms.objects.get(id=id)
            room.delete()
            return Response({"message": "Room deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Rooms.DoesNotExist:
            return Response({"message": "Room not found"}, status=status.HTTP_404_NOT_FOUND)


class OfferRoomsList(APIView):
    
    def get(self, request):
        id = request.GET.get('id')

        # 모든 방 내놓기 글 최신순으로 정렬
        if id == "all":
            rooms = Rooms.objects.filter(category="방 내놓기").order_by("-date")
            serializer = RoomsSerializer(rooms, many=True)

            return Response(serializer.data)
        
        # 특정 방 내놓기 글
        elif id.isdigit():
            room = Rooms.objects.filter(pk=id, category="방 내놓기기")
            serializer = RoomsSerializer(room)

            return Response(serializer.data)

        # 특정 구에 있는 방 내놓기 글 최신순으로 정렬
        else:
            id_values = id.split(',')

            rooms = Rooms.objects.filter(address__icontains=id_values[0], category="방 내놓기")

            if len(id_values) != 1:  # id 값이 여러 개일 경우
                for i in id_values[1:]:
                    rooms = rooms | Rooms.objects.filter(address__icontains=i, category="방 내놓기")

            sorted_rooms = sorted(rooms, key=lambda room: room.date, reverse=True)
            serializer = RoomsSerializer(sorted_rooms, many=True)

            return Response(serializer.data)
        
class OfferRoomsAdd(APIView):
    def post(self, request):
        data = request.data  # 요청 데이터 추출 (실제 데이터 형식에 맞게 수정해야 합니다.)
        new_room = Rooms.objects.create(
            ruser = data.get('user'), # user_id
            address = data.get('address'),
            area = data.get('area'), # 평수
            deposit = data.get('deposit'), # 보증금
            monthly_rent = data.get('monthly_rent'), # 월세금
            maintenance_cost = data.get('maintenance_cost'), # 관리비
            type = data.get('type'), # 임대유형
            start_date = data.get('start_date'),
            end_date = data.get('end_date'),
            structure = data.get('structure'), # 방 구조
            women_only = data.get('women_only'),
            sold = data.get(''),
            category = data.get('category'), # 방 구하기
            title = data.get('title'),
            comment = data.get('comment'),
            interest = data.get('interest'),
        )
        serialized_room = RoomsSerializer(new_room).data
        return Response({'message': 'Room added successfully', 'room': serialized_room})

class OfferRoomsPut(APIView):
    # 특정 내놓기 글 수정
    def put(self, request):
        id = request.GET.get('id')

        try:
            room = Rooms.objects.get(id=id)
        except Rooms.DoesNotExist:
            return Response({"message": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = RoomsSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OfferRoomsDelete(APIView):
    # 특정 내놓기 글 삭제
    def delete(self, request):
        id = request.GET.get('id')

        try:
            room = Rooms.objects.get(id=id)
            room.delete()
            return Response({"message": "Room deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Rooms.DoesNotExist:
            return Response({"message": "Room not found"}, status=status.HTTP_404_NOT_FOUND)


class PromotionRoomsList(APIView):
    
    def get(self, request):
        id = request.GET.get('id')

        # 모든 방 홍보 글 최신순으로 정렬
        if id == "all":
            rooms = Rooms.objects.filter(category="방 홍보").order_by("-date")
            serializer = RoomsSerializer(rooms, many=True)

            return Response(serializer.data)
        
        # 특정 방 홍보 글
        elif id.isdigit():
            room = Rooms.objects.filter(pk=id, category="방 홍보")
            serializer = RoomsSerializer(room)

            return Response(serializer.data)

        # 특정 구에 있는 방 홍보 글 최신순으로 정렬
        else:
            id_values = id.split(',')

            rooms = Rooms.objects.filter(address__icontains=id_values[0], category="방 홍보")

            if len(id_values) != 1:  # id 값이 여러 개일 경우
                for i in id_values[1:]:
                    rooms = rooms | Rooms.objects.filter(address__icontains=i, category="방 홍보")

            sorted_rooms = sorted(rooms, key=lambda room: room.date, reverse=True)
            serializer = RoomsSerializer(sorted_rooms, many=True)

            return Response(serializer.data)
        
class PromotionRoomsAdd(APIView):
    def post(self, request):
        data = request.data  # 요청 데이터 추출 (실제 데이터 형식에 맞게 수정해야 합니다.)
        new_room = Rooms.objects.create(
            ruser = data.get('user'), # user_id
            address = data.get('address'),
            area = data.get('area'), # 평수
            deposit = data.get('deposit'), # 보증금
            monthly_rent = data.get('monthly_rent'), # 월세금
            maintenance_cost = data.get('maintenance_cost'), # 관리비
            type = data.get('type'), # 임대유형
            structure = data.get('structure'), # 방 구조
            women_only = data.get('women_only'),
            category = data.get('category'), # 방 구하기
            title = data.get('title'),
            comment = data.get('comment'),
            interest = data.get('interest'),
        )
        serialized_room = RoomsSerializer(new_room).data
        return Response({'message': 'Room added successfully', 'room': serialized_room})

class PromotionRoomsPut(APIView):
    # 특정 홍보 글 수정
    def put(self, request):
        id = request.GET.get('id')

        try:
            room = Rooms.objects.get(id=id)
        except Rooms.DoesNotExist:
            return Response({"message": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = RoomsSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PromotionRoomsDelete(APIView):
    # 특정 홍보 글 삭제
    def delete(self, request):
        id = request.GET.get('id')

        try:
            room = Rooms.objects.get(id=id)
            room.delete()
            return Response({"message": "Room deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Rooms.DoesNotExist:
            return Response({"message": "Room not found"}, status=status.HTTP_404_NOT_FOUND)


class MyInterestList(APIView):

    def get(self, request):
        now = timezone.now()
        hours_48_ago = now - timedelta(hours=48)

        interest_rooms = Rooms.objects.filter(date__range=(hours_48_ago, now)).order_by('-interest')
        serializer = RoomsSerializer(interest_rooms, many=True)


        return Response(serializer.data)