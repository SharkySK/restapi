from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url','username','email','groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url','name')


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = "__all__"


class User_accountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_account
        fields = "__all__"


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"


class Activity_logSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity_log
        fields = "__all__"


class Booking_scheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking_schedule
        fields = "__all__"


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = "__all__"


class BridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bridge
        fields = "__all__"


class Opening_hoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opening_hours
        fields = "__all__"


class Billing_optSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing_opt
        fields = "__all__"


class Package_optSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package_opt
        fields = "__all__"
