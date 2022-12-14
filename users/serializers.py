from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Users


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'first_name', 'last_name', 'email')
        # print(fields)
