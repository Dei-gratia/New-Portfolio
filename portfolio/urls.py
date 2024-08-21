from django.urls import path
from .views import index, download_resume

urlpatterns = [
	path('', index),
	path('download/resume/', download_resume, name='download_resume'),
]