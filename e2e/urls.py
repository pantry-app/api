from django.conf.urls import url

from .views import reset

urlpatterns = [url("reset/", reset)]
