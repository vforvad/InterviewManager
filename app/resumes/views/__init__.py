from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404
from resumes.serializers import ResumesSerializer, ResumeSerializer
from rest_framework.decorators import list_route
from resumes.models import Resume
from resumes.index import ResumesIndex
from resumes.search import ResumesSearch

from .resumes import ResumeViewSet
