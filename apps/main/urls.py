from django.urls import path
from apps.main import views

urlpatterns = [
    path('', views.MainTemplateView.as_view(), name='home')
]
