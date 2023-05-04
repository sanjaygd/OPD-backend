from django.contrib import admin
from django.urls import path

from .views import VisitListView,CreateVisitApiView, CreateDoctorApiView, ListDoctorApiView


app_name = 'opd'
urlpatterns = [
    path('', VisitListView.as_view(), name='vist-list'),
    path('create/', CreateVisitApiView.as_view(), name='create-visit'),
    path('create-doctor/', CreateDoctorApiView.as_view(), name='create-doctor'),
    path('list-doctor/', ListDoctorApiView.as_view(), name='list-doctor'),
]
