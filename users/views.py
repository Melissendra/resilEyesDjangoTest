from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import UserSerializer


class UserList(ListCreateAPIView):
    # Get the users list and create a new one if wanted
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    # Getting the detail of a user
    queryset = User.objects.all()
    serializer_class = UserSerializer


