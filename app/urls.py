from django.urls import path
from .views import *


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('news', AllNewsView.as_view(), name='all_news'),
    path('news/<int:pk>', NewsView.as_view(), name='news'),
    path('Participant/<int:pk>', ParticipantView.as_view(), name='participant'),
    # path('about-us', AboutUsView.as_view(), name='about_us'),
    path('events/', EventsView.as_view(), name='events'),
    path('participants', ParticipantsView.as_view(), name='participants'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event'),
    path('results/', ResultsView.as_view(), name='results'),
    path('results/<int:pk>', ResultDetailView.as_view(), name='result'),
    path('set-language/', set_language, name='set_language'),
]