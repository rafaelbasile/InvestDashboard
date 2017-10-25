from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from .models import CompanySegment

# Serializers define the API representation.
class CompanySegmentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CompanySegment
		fields = ('name',)

