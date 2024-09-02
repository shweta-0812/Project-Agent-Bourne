from pydantic import ValidationError
from typing import Dict
from client.pydantic_models.client_pydantic_model import CreateClientDetailSchema, UpdateClientDetailSchema, \
    FetchClientDetailSchema, FetchAllClientDetailSchema, GetOrCreateClientDetailSchema

from client.repos.client_detail_repo import create_client_detail, update_client_detail, fetch_all_client_detail, \
    fetch_client_detail

from common_utils import filter_none_values


def create_new_client(client_create_data: dict):
    try:
        client_data = CreateClientDetailSchema(**client_create_data)
    except ValidationError as e:
        print("Validation error:", e)
        return None

    print("Validated client:", client_data)
    filtered_client_data = filter_none_values(client_data.__dict__)
    return create_client_detail(filtered_client_data)


def update_client(client_data: dict) -> Dict:
    try:
        client = UpdateClientDetailSchema(**client_data)
    except ValidationError as e:
        print("Validation error:", e)
        return None

    print("Validated client:", client)
    updated_client = update_client_detail(**client_data)
    return updated_client.__dict__


def get_client(client_filters: dict):
    try:
        client_filters = FetchClientDetailSchema(**client_filters)
        client_filters = filter_none_values(client_filters.__dict__)
    except ValidationError as e:
        print("Validation error:", e)
        return None

    print("Validated client:", client_filters)
    return fetch_client_detail(client_filters)


def get_all_clients(client_filters: dict):
    try:
        client_filters = FetchAllClientDetailSchema(**client_filters)
        client_filters = filter_none_values(client_filters.__dict__)
    except ValidationError as e:
        print("Validation error:", e)
        return None

    print("Validated client:", client_filters)
    client_details_qs = fetch_all_client_detail(client_filters)
    all_clients = []

    if client_details_qs.first() is None:
        return all_clients

    for c in list(client_details_qs):
        client = {'id': c.id,
                  'domain': c.domain,
                  'name': c.name}
        all_clients.append(client)
    return all_clients


def get_or_create_client(client_data: dict):
    try:
        client_data = GetOrCreateClientDetailSchema(**client_data)
        client_data = filter_none_values(client_data.__dict__)
    except ValidationError as e:
        print("Validation error:", e)
        return None
    print("Validated client_data:", client_data)
    is_new_client = False
    client_details = fetch_client_detail(client_data)
    client = client_details.first()
    if client is None:
        is_new_client = True
        new_client = create_new_client(client_create_data=client_data)
        return new_client, is_new_client
    return client, is_new_client
