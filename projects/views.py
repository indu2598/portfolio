from django.shortcuts import render
from rest_framework import viewsets
from projects.models import ProjectInfo
from projects.serializers import ProjectInfoSerializer
# Create your views here.


class ProjectInfoViewset(viewsets.ModelViewSet):
    queryset = ProjectInfo.objects.filter(show = True)
    serializer_class = ProjectInfoSerializer