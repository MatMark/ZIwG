from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    '''
    This class is serializer for User model
    '''
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    '''
    This class is serializer for Group model
    '''
    class Meta:
        model = Group
        fields = ['url', 'name']