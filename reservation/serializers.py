from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    reservation_name = serializers.CharField(source='reservation_for', read_only=True)
    class Meta:
        model = Reservation
        fields = '__all__'
