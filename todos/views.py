from rest_framework import viewsets
from django_modals.models import Todo
from django_modals.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Todo instances.
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
