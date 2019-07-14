from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response

GOOGLE_APPLICATION_CREDENTIALS = '/Users/markmc/Repos/sandbox/indigo-scribe'


class ProjectViewSet(viewsets.ModelViewSet):
    """A viewset for interacting with project objects."""
    queryset = User.objects.all()


class ContentBlockViewSet(viewsets.ModelViewSet):
    """A viewset for managing content blocks."""
    queryset = User.objects.all()

    def store(self):
        """File handling for content blocks."""
        test = default_storage.exists('storage_test')
        return Response(test)


def index(request):
    """Landing page."""
    return HttpResponse("Hello, world. You're at the My Project landing page.")

