from api.serializers import ToDoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models import ToDo


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsAuthenticated,)
