from client.models.client_detail_model import ClientDetailModel
from user.models.user_detail_model import UserDetailModel

UserDetailModel.objects.all().delete()
ClientDetailModel.objects.all().delete()

# 1. Create Operations
print("Creating a new client")
new_client = ClientDetailModel.objects.create(
    domain='example.com',
    name='Example Client',
    timezone='UTC'
)
print(new_client.__dict__)

print("Creating a new user and associating it with the new client")
new_user1 = UserDetailModel.objects.create(
    name='John',
    email='john.doe@example.com',
    password='hashed_password_here',
    profile_pic_url='http://example.com/profile_pic.jpg',
    client=new_client,
    is_admin=True
)
new_user2 = UserDetailModel.objects.create(
    name='John',
    email='john.doe2@example.com',
    password='hashed_password_here',
    profile_pic_url='http://example.com/profile_pic2.jpg',
    client=new_client,
    is_admin=True
)

print(new_user1.__dict__)

# 2. Read Operations
print("::::Get All Users:::::")
users = UserDetailModel.objects.all()
print(users)

#
print("::::Get a Specific User by Email:::::")
user = UserDetailModel.objects.get(email='john.doe@example.com')
print(user.__dict__)

print("::::Get Users Associated with a Specific Client:::::")
client_users = UserDetailModel.objects.filter(client=new_client)
print(client_users)

print("::::Get a User’s Client Details:::::")
user_client = user.client
print(user_client.__dict__)

# 3. Update Operations
print("Update a User's Name")
user.name = 'Smith'
user.save()
print(user.__dict__)

print("Update Client Details")
client = ClientDetailModel.objects.get(id=new_client.id)
print(client.domain)
client.domain = 'new-domain.com'
client.save()
print(client.domain)

# 4. Delete Operations
print("Delete a User")
print(user)
user.delete()
del_user = UserDetailModel.objects.get(email='john.doe@example.com')
print(del_user)

print("Delete a Client and Cascade to Users")
# This will also delete all related users due to `on_delete=models.CASCADE`
print(client)
client.delete()
del_client = ClientDetailModel.objects.get(id=new_client.id)
print(del_client)

# 5. Related Operations
print("Get All Users for a Client")
client_users = new_client.users.all()
print(client_users)

print("complete")
