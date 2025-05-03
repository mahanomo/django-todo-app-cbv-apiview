from todo_app.models import AddTodo
from rest_framework import permissions, viewsets
from .permissions import IsOwnerOrReadOnly

from .serializers import TodoTaskSerializer


class TodoTaskModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AddTodo.objects.all()
    serializer_class = TodoTaskSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]