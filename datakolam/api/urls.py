from django.urls import path
from datakolam.api.views import HistoryListAPIView,HomeListAPIView

urlpatterns=[
    path('history/', HistoryListAPIView.as_view(), name='history-list'),
    path('home/', HomeListAPIView.as_view(), name='home-list'),
]