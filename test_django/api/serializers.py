from rest_framework.serializers import ModelSerializer

from api.models import Connection

class ConnectionSerializer(ModelSerializer):
    class Meta:
        model = Connection
        fields = ('id', 'name', 'type')
        extra_kwargs = {
            'id': {'read_only': True}
        }