from django.urls import include, path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'facility', views.FacilityViewSet)
router.register(r'bridge', views.BridgeViewSet)
# Wire up our API using automatic URL routing
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls)
    path('', include(router.urls))
]
