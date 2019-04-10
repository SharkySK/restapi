from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'facility', views.FacilityViewSet)
router.register(r'bridge', views.BridgeViewSet)
router.register(r'equipment', views.EquipmentViewSet)
router.register(r'user_account', views.User_accountViewSet)
router.register(r'activity_log', views.Activity_logViewSet)
router.register(r'booking_schedule', views.Booking_scheduleViewSet)
router.register(r'booking_opt', views.Booking_optViewSet)
router.register(r'training', views.TrainingViewSet)
router.register(r'package', views.Package_optViewSet)
router.register(r'billing_opt', views.Billing_optViewSet)
router.register(r'opening_hours', views.Opening_hoursViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'user_ver/<int:pk>/', views.User_verificationViewSet)

# Wire up our API using automatic URL routing
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
