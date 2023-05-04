from django.urls import path

from .views import CreatePatientApiView

app_name = 'patent_info'
urlpatterns = [
    path('', CreatePatientApiView.as_view(), name='list-create-patient'),   
]
