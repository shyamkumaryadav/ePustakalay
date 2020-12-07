from rest_framework import generics, versioning, permissions, serializers, mixins
from django.contrib.auth import get_user_model
from emanagement.utils import ReadOnly


class UserSerializers(serializers.ModelSerializer):
    '''
    The Serializer of `User`
    '''
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super(UserSerializers, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserAPI(generics.CreateAPIView, mixins.UpdateModelMixin, mixins.CreateModelMixin):
    """
    E-Management `User` ViewSet
    """
    serializer_class = UserSerializers
