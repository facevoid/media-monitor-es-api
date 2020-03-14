

def get_object_from_hits(hits):
    hits = hits['hits']['hits']
    results = []
    for result in hits:
        response_data = {}
        result = result['_source']
        response_data['url'] = result['url']
        response_data['category'] = result['category']
        response_data['title'] = result['title']
        response_data['source_url'] = result['source_url']
        response_data['top_img'] = result['top_img']
        response_data['content'] = result['content']
        response_data['publish_date'] = result['publish_date']
        response_data['sentiment'] = result['sentiment']
        response_data['summary'] = result['summary']

        results.append(response_data)
    print(len(results))
    return results

def process_suggestion_from_response(response):
    suggestion = []
    for data in response:
        for option in data['options']:
            suggestion.append(option['text'])
    return suggestion
        
