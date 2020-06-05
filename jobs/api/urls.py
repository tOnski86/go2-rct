from django.urls import include, path
from rest_framework.routers import DefaultRouter
from jobs.api.views import JobViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls))
]