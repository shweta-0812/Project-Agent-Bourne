# from weaviate import EmbeddedOptions # Embedded Weaviate is a new deployment model that runs a Weaviate instance
# from your application code rather than from a stand-alone Weaviate server installation.
from dotenv import load_dotenv, find_dotenv
import openai
from utils import get_env_key
import memory.weaviate.db_schemas as SCHEMAS
import weaviate

_ = load_dotenv(find_dotenv())  # read local .env file

WEAVIATE_API_KEY = get_env_key('WEAVIATE_API_KEY')
WEAVIATE_DB_HOST = get_env_key('WEAVIATE_DB_HOST')
WEAVIATE_DB_PORT = get_env_key('WEAVIATE_DB_PORT')
WEAVIATE_DB_HTTP_SECURE = get_env_key('WEAVIATE_DB_HTTP_SECURE')
WEAVIATE_DB_GRPC_HOST = get_env_key('WEAVIATE_DB_GRPC_HOST')
WEAVIATE_DB_GRPC_PORT = get_env_key('WEAVIATE_DB_GRPC_PORT')
WEAVIATE_DB_GRPC_SECURE = get_env_key('WEAVIATE_DB_GRPC_SECURE')
WEAVIATE_API_KEY = get_env_key('WEAVIATE_API_KEY')

OPENAI_API_KEY = get_env_key('OPENAI_API_KEY')
OPENAI_API_BASE = get_env_key('OPENAI_API_BASE')
openai.api_key = get_env_key

COHERE_API_KEY = get_env_key('COHERE_API_KEY')
COHERE_API_BASE = get_env_key('COHERE_API_BASE')


'''
    initialise client
    # headers={
    #     "X-OpenAI-Api-Key": OPENAI_API_KEY  # Or any other inference API keys,
    #     "X-OpenAI-BaseURL": OPENAI_API_BASE,
    #     "X-Cohere-Api-Key": "COHERE_API_KEY",
    #     "X-Cohere-BaseURL": "COHERE_API_BASE"
    # }

'''


def initialise_weaviate_client(open_ai=False, cohere=False):
    headers = {}
    if open_ai:
        headers["X-OpenAI-Api-Key"] = OPENAI_API_KEY
        headers["X-OpenAI-BaseURL"] = OPENAI_API_BASE
    if cohere:
        headers["X-Cohere-Api-Key"] = COHERE_API_KEY
        headers["X-Cohere-BaseURL"] = COHERE_API_BASE

    return weaviate.connect_to_custom(
        http_host=WEAVIATE_DB_HOST,
        http_port=WEAVIATE_DB_PORT,
        http_secure=WEAVIATE_DB_HTTP_SECURE,
        grpc_host=WEAVIATE_DB_GRPC_HOST,
        grpc_port=WEAVIATE_DB_GRPC_PORT,
        grpc_secure=WEAVIATE_DB_GRPC_SECURE,
        auth_credentials=weaviate.auth.AuthApiKey(WEAVIATE_API_KEY),
        headers=headers

    )


'''
Create an embedded instance of Weaviate vector database
'''


def create_weaviate_client():
    wclient = initialise_weaviate_client()
    try:
        print(f"Client created? {wclient.is_ready()}")
        meta_data = wclient.get_meta()
    finally:
        # Ensure the connection is closed
        wclient.close()
    return meta_data


def create_db_collection(schema_name):
    wclient = initialise_weaviate_client()
    try:
        if not wclient.schema.exists(schema_name):
            schema_class_obj = SCHEMAS.schema_name
            wclient.schema.create_class(schema_class_obj)
    finally:
        # Ensure the connection is closed
        wclient.close()
    return True


def reset_db_collection(schema_name):
    wclient = initialise_weaviate_client()
    try:
        # resetting the schema
        # CAUTION: This will delete your collection
        if wclient.schema.exists(schema_name):
            wclient.schema.delete_class(schema_name)
        schema_class_obj = SCHEMAS.schema_name
        wclient.schema.create_class(schema_class_obj)
    finally:
        # Ensure the connection is closed
        wclient.close()
    return True
