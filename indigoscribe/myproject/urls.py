from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from myproject.views import ProjectViewSet
from myproject.views import ContentBlockViewSet

router = DefaultRouter()
router.register(r'project', ProjectViewSet, basename='project')
router.register(r'block', ContentBlockViewSet, basename='project')

urlpatterns = [
    url(r'^', include(router.urls))
]