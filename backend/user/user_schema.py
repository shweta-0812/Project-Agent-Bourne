from graphene import ObjectType, String, Int, Boolean, Field, Mutation, List
from user.service.user_service import get_or_create_new_individual_user, update_user, get_all_users


# class UserDetailType(DjangoObjectType):
#     class Meta:
#         model = UserDetailModel

class CreateUserDetailType(ObjectType):
    id = Int()
    email = String()
    name = String()
    is_admin = Boolean()
    is_new_user = Boolean()


class UpdateUserDetailType(ObjectType):
    id = Int()
    email = String()
    name = String()
    is_admin = Boolean()


class GetUserDetailType(ObjectType):
    id = Int()
    email = String()
    name = String()
    is_admin = Boolean()
    user_type = Int()
    client_id = Int()
    profile_pic_url = String()
    last_login = String()


class SampleUserDetailType(ObjectType):
    id = Int()
    email = String()
    name = String()


class CreateUserDetail(Mutation):
    ok = Boolean()
    user_detail = Field(lambda: CreateUserDetailType)

    class Arguments:
        # define params for mutation
        name = String()
        email = String()
        profile_pic_url = String()
        is_admin = Boolean()
        status = Int()
        client_id = Int()

    def mutate(self, info, name,  email, profile_pic_url, is_admin,
               status, client_id):
        user_data = {
            "name": name,
            "email": email,
            "profile_pic_url": profile_pic_url,
            "is_admin": is_admin,
            "status": status,
        }
        user_detail = get_or_create_new_individual_user(user_data)
        return CreateUserDetail(user_detail=user_detail, ok=True)


class UpdateUserDetail(Mutation):
    user_detail = Field(lambda: UpdateUserDetailType)
    ok = Boolean()

    class Arguments:
        id = Int()
        name = String()
        profile_pic_url = String()
        is_admin = Boolean()
        status = Int()

    def mutate(self, info, id, name, profile_pic_url, is_admin,
               status):
        user_data = {
            "id": id,
            "name": name,
            "profile_pic_url": profile_pic_url,
            "is_admin": is_admin,
            "status": status,
        }
        updated_user_detail = update_user(user_data=user_data)
        ok = True
        return UpdateUserDetail(user_detail=updated_user_detail, ok=ok)


class Query(ObjectType):
    user_details = List(GetUserDetailType)
    sample_user_detail = Field(SampleUserDetailType)

    def resolve_user_details(self, info):
        user_filters = {}
        all_user_details = get_all_users(user_filters=user_filters)
        return all_user_details

    def resolve_sample_user_detail(self, info):
        return SampleUserDetailType(1, "shweta@test.com", "shweta singh")


class Mutation(ObjectType):
    create_user_detail = CreateUserDetail.Field()
    update_user_detail = UpdateUserDetail.Field()
