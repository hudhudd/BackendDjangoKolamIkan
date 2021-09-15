from rest_framework import serializers
from datakolam.models import Datakol
from django.contrib.auth.models import User

class HistoryPage(serializers.ModelSerializer):
    class Meta :
        model = Datakol
        fields = '__all__'