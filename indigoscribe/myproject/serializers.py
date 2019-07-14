"""Serializers for MyProject app."""
from rest_framework import serializers

from myproject.models import ContentBlock, Project


class ContentBlockSerializer(serializers.ModelSerializer):
    """Serializer for Content Block objects."""
    class Meta:
        """Association between serializer and model."""
        model = ContentBlock
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Projects."""
    class Meta:
        """Association between serializer and model."""
        model = Project
        fields = '__all__'
