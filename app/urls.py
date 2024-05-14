from django.urls import path
from .views import ApplicationCreateView, EnvironmentCreateView, InstanceCreateView, EnvironmentVariableCreateView

urlpatterns = [
    path('applications/', ApplicationCreateView.as_view(), name='create-application'),
    path('environments/', EnvironmentCreateView.as_view(), name='create-environment'),
    path('instances/', InstanceCreateView.as_view(), name='create-instance'),
    path('variables/', EnvironmentVariableCreateView.as_view(), name='create-variable'),
]
