from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FacilityViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Facility.objects.all()
    sc = FacilitySerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Equipment.objects.all()
    sc = EquipmentSerializer


class User_accountViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = User_account.objects.all()
    sc = User_accountSerializer


class Activity_logViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Activity_log.objects.all()
    sc = Activity_logSerializer


class Booking_scheduleViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Booking_schedule.objects.all()
    sc = Booking_scheduleSerializer


class Booking_optViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Booking_opt.objects.all()
    sc = Billing_optSerializer


class TrainingViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Training.objects.all()
    sc = TrainingSerializer


class Package_optViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Package_opt.objects.all()
    sc = Package_optSerializer


class Billing_optViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Billing_opt.objects.all()
    sc = Billing_optSerializer


class Opening_hoursViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Opening_hours.objects.all()
    sc = Opening_hoursSerializer


class BridgeViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Bridge.objects.all()
    sc = BridgeSerializer