from django.conf.urls import url, include
from rest_framework import  serializers
from .models import CompanySegment

# Serializers define the API representation.
class CompanySegmentSerializer(serializers.Serializer):

	class Meta:
		model = CompanySegment
		fields = ('name''',)

