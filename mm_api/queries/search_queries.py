

def get_autocomplete_query(prefix):
    autocomplete_query = {
        "suggest": {
            "autocomplete" : {
                "prefix" : prefix, 
                "completion" : { 
                    "field" : "suggestor" 
                }
            }
        }
    }

    return autocomplete_query