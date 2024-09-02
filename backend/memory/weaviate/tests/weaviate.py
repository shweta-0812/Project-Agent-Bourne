from django.http import JsonResponse
import sys

from backend.memory.weaviate.client import create_weaviate_client, create_db_collection, reset_db_collection,\
    load_sample_data
from backend.memory.weaviate.search.base_search import search


def check_client_abilities():
    schema_name = 'questions'
    ability = "create_db_schema"
    match ability:
        case "create_db_schema":
            response = create_db_collection(schema_name)
            return JsonResponse({'status': 'success', 'response': response})
        case "reset_db_schema":
            response = reset_db_collection(schema_name)
            return JsonResponse({'status': 'success', 'response': response})
        case "load_sample_data":
            count = load_sample_data(schema_name)
            return JsonResponse({'status': 'success', 'data_count': count})
        case "search":
            schema_name = "questions"
            properties = ["question", "answer"]
            # query = "animal"
            query = {"concepts": ["animal"]}
            search_type = 'dense'
            limit = 1
            response = search(schema_name=schema_name, properties=properties,
                              query=query, search_type=search_type,
                              limit=limit)
            return JsonResponse({'status': 'success', 'response': response})
        case _:
            meta_data = create_weaviate_client()
            return JsonResponse({'status': 'success', 'meta_data': meta_data})


def main():
    # Get the command-line arguments
    arg = sys.argv
    check_client_abilities(arg)


if __name__ == '__main__':
    main()
