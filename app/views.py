from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from django.urls import reverse

class MainView(generic.ListView):
    template_name = 'main.html'
    model = News
    context_object_name = 'news_list'

    def get_news_queryset(self):
        queryset = News.objects.filter(news_for_main=True).order_by('-created_at')
        return queryset
    
    def get(self, request):
        return render(request, self.template_name, {'news_list': self.get_news_queryset()})
    
class AllNewsView(generic.ListView):
    template_name = 'all_news.html'
    model = News
    context_object_name = 'all_news_list'
    paginate_by = 4

    def get_queryset(self):
        queryset = News.objects.all().order_by('-created_at')
        return queryset
    
class ParticipantsView(generic.ListView):
    template_name = 'participants.html'
    model = Participant
    context_object_name = 'participants_list'
    paginate_by = 4

    def get_queryset(self):
        queryset = Participant.objects.all().order_by('-pos_index')
        return queryset
    
class EventsView(generic.ListView):
    template_name = 'events.html'
    model = Event
    context_object_name = 'events_list'
    paginate_by = 4
    
    def get_queryset(self):
        queryset = Event.objects.all().order_by('-created_at')
        return queryset

class EventDetailView(generic.DetailView):
    model = Event
    template_name = "event.html"
    context_object_name = "event"

class NewsView(generic.DetailView):
    template_name = 'news.html'
    model = News
    context_object_name = 'news'
    
class ParticipantView(generic.DetailView):
    template_name = 'participant.html'
    model = Participant
    context_object_name = 'participant'
    
def set_language(request):
    """
    Простейший view для переключения языка.
    Ожидает GET-параметр ?lang=ru|kk|en и сохраняет его в сессии.
    Затем возвращает на предыдущую страницу (или на корень).
    """
    lang = request.GET.get('lang', 'ru')
    if lang in ('ru', 'kk'):
        request.session['lang'] = lang
    return redirect(request.META.get('HTTP_REFERER', reverse('main')))