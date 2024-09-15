from rest_framework.generics import CreateAPIView
from .serializers import UserRegisterModelSerializer
from luffycityapi.luffycityapi.apps.users.models import User


class UserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterModelSerializer