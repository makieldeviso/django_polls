from django.urls import path
from . import views

# url pattern for polls_app views
urlpatterns = [
    path('', views.index, name='index')
]