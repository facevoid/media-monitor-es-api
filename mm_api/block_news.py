from django.shortcuts import render
from django.http import HttpResponse
import json

# from elasticsearch_dsl import Document, Date, Integer, Keyword, Text
# from elasticsearch_dsl.connections import connections
from mm_api.queries.block_queries import match_all_query
from mm_api.utils import get_object_from_hits

from elasticsearch import Elasticsearch

es_connection = Elasticsearch([{'host': 'ip', 'port': 1234}])

#this one is done for demo please complete others 
def index(request):
    result = es_connection.search(index='mm_el_dev', body=json.dumps(match_all_query))  
    return HttpResponse(json.dumps(get_object_from_hits(result)))

def get_top_news(request):
    pass

def get_recent_news(request):
    #make sorted based on dates
    pass

def categorical_news(request):
    pass

def get_subscribed_topic_news(request):
    pass
