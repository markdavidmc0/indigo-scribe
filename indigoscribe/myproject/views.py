from environs import Env

from rest_framework import viewsets
from rest_framework.response import Response

from myproject.models import ContentBlock, Project
from myproject.serializers import ContentBlockSerializer, ProjectSerializer

env = Env()
env.read_env()  # read .env file, if it exists

GOOGLE_APPLICATION_CREDENTIALS = env('GOOGLE_APPLICATION_CREDENTIALS')


def index(request) -> Response:
    """Landing page."""
    return Response("Hello, world. You're at the My Project landing page.")


class ProjectViewSet(viewsets.ModelViewSet):
    """A viewset for interacting with project objects."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ContentBlockViewSet(viewsets.ModelViewSet):
    """A viewset for managing content blocks."""
    queryset = ContentBlock.objects.all()
    serializer_class = ContentBlockSerializer
