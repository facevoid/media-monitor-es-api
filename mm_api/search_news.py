from django.http import HttpResponse
import json

from mm_api.queries.search_queries import get_autocomplete_query
from mm_api.utils import get_object_from_hits, process_suggestion_from_response

from elasticsearch import Elasticsearch

es_connection = Elasticsearch([{'host': 'ip:addr', 'port': 1234}])

def get_autocomplete_suggestion(request):
    query = "জি"
    query = get_autocomplete_query(prefix=query)

    result = es_connection.search(index='mm_el_dev', body=json.dumps(query))
    return HttpResponse(json.dumps(process_suggestion_from_response(result['suggest']['autocomplete'])))

def get_search_result(request):
    #make boost on title field
    pass
