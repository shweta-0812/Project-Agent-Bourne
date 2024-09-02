from graphene import Int, String, Boolean, List, Mutation, ObjectType, Field
from client.service.client_service import get_client, get_all_clients, update_client
from main.models.base_model import Status


# class ClientDetailType(DjangoObjectType):
#     class Meta:
#         model = ClientDetailModel


class ClientDetailType(ObjectType):
    id = Int()
    uuid = String()
    name = String()
    domain = String()
    status = String()


class UpdateClientDetail(Mutation):
    client_detail = Field(lambda: ClientDetailType)
    ok = Boolean()

    class Arguments:
        id: Int()
        name = String()

    def mutate(self, info, id, name):
        updated_client_detail = update_client({'id': id, 'name': name})
        return UpdateClientDetail(client_detail=updated_client_detail, ok=True)


class Query(ObjectType):
    all_client_details = List(ClientDetailType)
    client_detail = Field(ClientDetailType)

    def resolve_all_client_details(self, info):
        return get_all_clients({'status': Status.ACTIVE})

    def resolve_client_detail(self, info):
        return get_client({'status': Status.ACTIVE})


class Mutation(ObjectType):
    update_client_detail = UpdateClientDetail.Field()
