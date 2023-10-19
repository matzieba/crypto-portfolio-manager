from drf_writable_nested import WritableNestedModelSerializer

from crypto_api.models import User


class UserSerializer(WritableNestedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

