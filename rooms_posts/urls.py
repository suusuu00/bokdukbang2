from django.urls import path
from .views import *

app_name = "rooms_posts"

urlpatterns = [
    path("find-rooms/", FindRoomsList.as_view(), name="find_rooms_list"),
    path("find-rooms/add/", FindRoomsAdd.as_view(), name="find_rooms_add"),
    path("find-rooms/modify/", FindRoomsPut.as_view(), name="find_rooms_put"),
    path("find-rooms/delete/", FindRoomsDelete.as_view(), name="find_rooms_delete"),

    path("offer-rooms/", OfferRoomsList.as_view(), name="offer_rooms_list"),
    path("offer-rooms/add/", OfferRoomsAdd.as_view(), name="offer_rooms_add"),
    path("offer-rooms/modify/", OfferRoomsPut.as_view(), name="offer_rooms_put"),
    path("offer-rooms/delete/", OfferRoomsDelete.as_view(), name="offer_rooms_delete"),

    path("promotion-rooms/", PromotionRoomsList.as_view(), name="promotion_rooms_list"),
    path("promotion-rooms/add/", PromotionRoomsAdd.as_view(), name="promotion_rooms_add"),
    path("promotion/modify/", PromotionRoomsPut.as_view(), name="promotion_rooms_put"),
    path("promotion/delete", PromotionRoomsDelete.as_view(), name="promotion_rooms_delete"),

    path("interest-post/", MyInterestList.as_view(), name="my_interest_list")
]
