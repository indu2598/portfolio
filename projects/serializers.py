from django.db import models
from django.db.models import fields
from rest_framework import serializers
from projects.models import ProjectInfo

class ProjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInfo
        fields = ['id','name','description','github','demo','image']