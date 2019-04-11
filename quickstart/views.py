from rest_framework import viewsets
from .serializers import *
from .models import *

from rest_framework.decorators import action
from rest_framework.response import Response


class testViewSet(viewsets.ModelViewSet):
    """
    Returns 200 or 400
    """
    queryset = Test.objects.all()
    serializer_class = TestSerializer


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


class User_verificationViewSet(viewsets.ModelViewSet):
    """
    Return user authorised or not
    """
    serializer_class = User_verificationSerializer

    def get_queryset(self):
        uid_tag, place = self.kwargs['uid_Tag', 'place']
        queryset = User_account.objects.filter(uid_tag=uid_tag)
        if queryset:
            return queryset
        else:
            return Response("No user Found", 404)

    @action(detail=True, methods=['post'])
    def add_key(self):
        uid, tag = self.kwargs['uid', 'uid_Tag']
        queryset = User_account.objects.filter(id=uid)
        if queryset:
            queryset.uid_Tag(tag)
            queryset.save()
            return Response("UID_tag set!", 200)
        else:
            return Response("No user with this ID", 400)


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
