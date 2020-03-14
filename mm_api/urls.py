from django.urls import path

from . import search_news
from . import block_news

urlpatterns = [
    path('', block_news.index, name='index'),
    path('get_top_news', block_news.get_top_news, name='top_news'),
    path('get_recent_news', block_news.get_recent_news, name='recent_news'),
    path('get_autocomplete_suggestion', search_news.get_autocomplete_suggestion, name='autocomplete')
]