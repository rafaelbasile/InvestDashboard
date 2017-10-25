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


class CompanySegmentViewSet(viewsets.ModelViewSet):
	queryset = CompanySegment.objects.all()
	serializer_class = CompanySegmentSerializer