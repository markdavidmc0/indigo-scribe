from django.db import models


class Project(models.Model):
    """Writing project."""

    TYPE_CHOICES = (
        ('book', 'book'),
        ('article', 'article'),
        ('short_story', 'short_story'),
        ('short_piece', 'short_piece'),
        ('poem', 'poem')
    )

    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    project_type = models.TextField(choices=TYPE_CHOICES, default="book", max_length=200)
    email = models.EmailField(max_length=254)
    created = models.DateTimeField('date created')


class ContentBlock(models.Model):
    """Content block in a writing project."""

    content_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    content = models.TextField()
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='blocks', max_length=100)
    created = models.DateTimeField('date created')
