from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import CompanySegment

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class CompanySegmentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CompanySegment
		fields = ('name',)