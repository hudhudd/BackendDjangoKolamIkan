from rest_framework import generics
from datakolam.models import Datakol
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from datakolam.api.serializers import HistoryPage
from django.contrib.auth.models import User

class HistoryListAPIView(generics.ListAPIView):
    serializer_class = HistoryPage
    def get_queryset(self):
        user = self.request.user
        return Datakol.objects.get_queryset().filter(owner = user)


class HomeListAPIView(generics.ListAPIView):
    serializer_class = HistoryPage
    def get_queryset(self):
        user = self.request.user
        return Datakol.objects.get_queryset().filter(owner = user).order_by('-upload_date')[:1]