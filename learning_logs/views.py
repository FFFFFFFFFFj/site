from django.shortcuts import render
from .models import Topic, Entry

def index(request):
    """Learning Log application home apge"""
    return render(request, 'index.html')

def topics(request):
    """Displays a list of topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)

def topic(request, topic_id):
    """Displays one topic and all its posts"""
    topic = Topic.objects.get(id=topic_id)
    enteries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', context)
