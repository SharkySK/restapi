from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class Booking_optSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking_opt
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


class FacilitySerializer(serializers.ModelSerializer):

    billopt = Billing_optSerializer(many=True)
    openh = Opening_hoursSerializer(many=True)
    bookopt = Booking_optSerializer(many=True)
    package = Package_optSerializer(many=True)

    class Meta:
        model = Facility
        fields = "__all__"


class EquipmentSerializer(serializers.ModelSerializer):

    bridge = BridgeSerializer(many=True)

    class Meta:
        model = Equipment
        fields = "__all__"


class TrainingSerializer(serializers.ModelSerializer):

    eq = EquipmentSerializer(read_only=True, many=True)

    class Meta:
        model = Training
        fields = "__all__"


class User_accountSerializer(serializers.ModelSerializer):

    bilopt = Billing_optSerializer(many=True)
    training = TrainingSerializer(many=True)
    pack = Package_optSerializer(many=True)

    class Meta:
        model = User_account
        fields = "__all__"


class User_verificationSerializer(serializers.ModelSerializer):

    pack = Package_optSerializer(many=True)
    training = TrainingSerializer(many=True)

    class Meta:
        model = User_account
        fields = "first_Name, last_Name, training, package_Opt"


class Activity_logSerializer(serializers.ModelSerializer):

    user = User_accountSerializer(many=True)
    eq = EquipmentSerializer(many=True)

    class Meta:
        model = Activity_log
        fields = "__all__"


class Booking_scheduleSerializer(serializers.ModelSerializer):

    user = User_accountSerializer(many=True)
    eq = EquipmentSerializer(many=True)

    class Meta:
        model = Booking_schedule
        fields = "__all__"
