from rest_framework import viewsets
from .serializers import *
from .models import *

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


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
    serializer_class = FacilitySerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class User_accountViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = User_account.objects.all()
    serializer_class = User_accountSerializer


class User_verification(APIView):
    """
    Return user authorised or not
    """

    def get_object(self, pk):
        try:
            return User_account.objects.get(pk=pk)
        except User_account.DoesNotExist:
            raise Http404

    def get(self, request,pk, format=None):
        user = User_account.get_object(pk)
        serializer = User_accountSerializer(user, data=request.data)
        return Response(serializer.data)


class Activity_logViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Activity_log.objects.all()
    serializer_class = Activity_logSerializer


class Booking_scheduleViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Booking_schedule.objects.all()
    serializer_class = Booking_scheduleSerializer


class Booking_optViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Booking_opt.objects.all()
    serializer_class = Billing_optSerializer


class TrainingViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class Package_optViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Package_opt.objects.all()
    serializer_class = Package_optSerializer


class Billing_optViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Billing_opt.objects.all()
    serializer_class = Billing_optSerializer


class Opening_hoursViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Opening_hours.objects.all()
    serializer_class = Opening_hoursSerializer


class BridgeViewSet(viewsets.ModelViewSet):
    """
    Return a list of all users.
    """
    queryset = Bridge.objects.all()
    serializer_class = BridgeSerializer
