from user.models.user_detail_model import UserDetailModel


def create_user_detail(user_create_data: dict):
    return UserDetailModel.objects.create(**user_create_data)


def get_user_detail(pk: int):
    return UserDetailModel.objects.get(pk=pk)


def update_user_detail(user_update_data: dict):
    user_detail = get_user_detail(pk=user_update_data['id'])

    if 'name' in user_update_data:
        user_detail.name = user_update_data['name']
    if 'profile_pic_url' in user_update_data:
        user_detail.profile_pic_url = user_update_data['profile_pic_url']
    if 'is_admin' in user_update_data:
        user_detail.is_admin = user_update_data['is_admin']
    if 'status' in user_update_data:
        user_detail.status = user_update_data['status']
    if 'last_login' in user_update_data:
        user_detail.last_login = user_update_data['last_login']

    user_detail.save()
    return user_detail


def fetch_user_detail(user_fetch_filters: dict):
    return UserDetailModel.objects.filter(**user_fetch_filters)


def fetch_all_user_detail(user_fetch_filters: dict):
    return UserDetailModel.objects.all(**user_fetch_filters)


def delete_user_detail(user_delete_filters: dict):
    return UserDetailModel.objects.get(**user_delete_filters)


def delete_all_user_detail(user_delete_filters: dict):
    return UserDetailModel.objects.all().delete(**user_delete_filters)
