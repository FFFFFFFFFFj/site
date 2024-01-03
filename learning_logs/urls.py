#"""Defianes  URL schemes for learning_logs."""
from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    #home page
    path('', views.index, name='index'),
    #page with a list of all topics
    path('topics/', views.topics, name='topics'),
    #page with detailed information on a specific topic
    path('topic/<int:topic_id>/', views.topic, name='topic'),
]
