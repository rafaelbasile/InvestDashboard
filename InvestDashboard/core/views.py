from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets, routers, serializers
from .models import CompanySegment
from .serializers import CompanySegmentSerializer

# Create your views here.

def home(request):
	title = 'Welcome'

	context = {
		"title": title,
	}
	return render(request, "index.html", context)


class CompanySegmentViewSet(viewsets.ViewSet):
	def list(self, request):
		queryset = CompanySegment.objects.all()
		serializer = CompanySegmentSerializer(queryset, many=True)
		return Response(serializer.data)


class CompanySegmentView(APIView):

	def get(self, request, format=None):
		data = {
			"value": CompanySegment.objects.all()
		}
		return Response(data)