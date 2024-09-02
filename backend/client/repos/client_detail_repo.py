from client.models.client_detail_model import ClientDetailModel


def create_client_detail(client_create_data: dict):
    client_detail = ClientDetailModel(**client_create_data)
    client_detail.save()
    return client_detail


def get_client_detail(pk: int):
    return ClientDetailModel.objects.get(pk=pk)


def update_client_detail(client_update_data: dict):
    client_detail = get_client_detail(pk=client_update_data['id'])

    if client_update_data['name']:
        client_detail.name = client_update_data['name']

    client_detail.save()
    return client_detail


def fetch_client_detail(client_fetch_filters: dict):
    return ClientDetailModel.objects.filter(**client_fetch_filters)


def fetch_all_client_detail(client_fetch_filters: dict):
    return ClientDetailModel.objects.all(**client_fetch_filters)


def delete_client_detail(client_delete_filters: dict):
    return ClientDetailModel.objects.filter(**client_delete_filters).delete()


def delete_all_client_detail(client_delete_filters: dict):
    return ClientDetailModel.objects.all().delete(**client_delete_filters)
