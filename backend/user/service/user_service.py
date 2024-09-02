from datetime import datetime, timezone
from pydantic import ValidationError
from typing import List, Dict
from user.pydantic_models.user_pydantic_model import CreateUserDetailSchema, UpdateUserDetailSchema, \
    FetchUserDetailSchema, FetchAllUserDetailSchema

from user.repos.user_detail_repo import create_user_detail, update_user_detail, fetch_all_user_detail, \
    fetch_user_detail

from common_utils import extract_and_validate_domain, filter_none_values

from client.service.client_service import get_or_create_client
from user.models.user_detail_model import UserTypes


def create_client_associated_user(user_data: dict):
    try:
        user_data = CreateUserDetailSchema(**user_data)
        user_data = filter_none_values(user_data.__dict__)
    except ValidationError as e:
        print("Validation error:", e)
        return None

    print("Validated user:", user_data)
    if user_data['client_id'] is None:
        # get user email domain
        domain = extract_and_validate_domain(user_data['email'])
        client, is_new_client = get_or_create_client({'domain': domain})
    else:
        client, is_new_client = get_or_create_client({'id': user_data['client_id']})

    user_data.client = client
    user_data.is_admin = True if is_new_client is True else False
    # create user for the client
    new_user = create_user_detail(user_data)
    return new_user


def get_or_create_new_individual_user(user_data: dict):
    # set user type as individual
    if 'user_type' not in user_data:
        user_data['user_type'] = UserTypes.INDIVIDUAL
    if 'is_admin' not in user_data:
        user_data['is_admin'] = True
    try:
        user_data = CreateUserDetailSchema(**user_data)
        user_data = filter_none_values(user_data.__dict__)
    except ValidationError as e:
        print("Validation error:", e)
        return None

    print("Validated user:", user_data)
    is_new_user = False

    user_details = fetch_user_detail(user_fetch_filters=user_data)
    user = user_details.first()
    if user is None:
        is_new_user = True
        new_user = create_user_detail(user_create_data=user_data)
        new_user = new_user.__dict__
        new_user['is_new_user'] = is_new_user
        return new_user
    user = user.__dict__
    user['is_new_user'] = is_new_user
    return user


def update_user(user_data: dict) -> Dict:
    try:
        user_data = UpdateUserDetailSchema(**user_data)
        user_data = filter_none_values(user_data.__dict__)
    except ValidationError as e:
        print("Validation error:", e)
        return None

    print("Validated user:", user_data)
    updated_user = update_user_detail(user_data)
    return updated_user.__dict__


def update_user_last_login(user_id: int) -> bool:
    update_user_detail(user_update_data={'id': user_id, 'last_login': datetime.now(timezone.utc)})
    return True


def get_user(user_filters: dict) -> Dict:
    try:
        user_filters = FetchUserDetailSchema(**user_filters)
        user_filters = filter_none_values(user_filters.__dict__)
    except ValidationError as e:
        print("Validation error:", e)
        return None

    print("Validated user:", user_filters)
    user = fetch_user_detail(user_filters)
    return user.__dict__


def get_all_users(user_filters: dict) -> List:
    try:
        user_filters = FetchAllUserDetailSchema(**user_filters)
        user_filters = filter_none_values(user_filters.__dict__)
    except ValidationError as e:
        print("Validation error:", e)
        return None

    print("Validated user:", user_filters)
    user_details_qs = fetch_all_user_detail(user_fetch_filters=user_filters)
    all_users = []
    if user_details_qs.first() is None:
        return all_users

    for u in list(user_details_qs):
        user = {'id': u.id,
                'email': u.email,
                'name': u.name,
                'is_admin': u.is_admin,
                'user_type': u.user_type,
                'client_id': u.client_id,
                'profile_pic_url': u.profile_pic_url,
                'last_login': u.last_login}
        all_users.append(user)
    return all_users
