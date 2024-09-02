from user.models.user_detail_model import UserDetailModel, UserWorkspaceMappingDetailModel
from client.models.client_detail_model import ClientDetailModel
from workspace.models.workspace_detail_model import WorkspaceDetailModel


UserDetailModel.objects.all().delete()
ClientDetailModel.objects.all().delete()
WorkspaceDetailModel.objects.all().delete()
UserWorkspaceMappingDetailModel.objects.all().delete()

print("Creating a new client")
new_client = ClientDetailModel.objects.create(
    domain='example.com',
    name='Example Client',
    timezone='UTC'
)

print("Creating a workspace for the new client")
new_workspace = WorkspaceDetailModel.objects.create(
    name='Main Workspace',
    client=new_client
)
print(new_workspace.__dict__)

print("Creating a workspace for the new client")
new_workspace2 = WorkspaceDetailModel.objects.create(
    name='Second Workspace',
    client=new_client
)

print("Creating a user and associating with a client")
new_user = UserDetailModel.objects.create(
    name='John',
    email='john.doe@example.com',
    password='hashed_password_here',
    client=new_client
)

print("Creating a user and associating with a client")
new_user2 = UserDetailModel.objects.create(
    name='Jane',
    email='jane.doe@example.com',
    password='hashed_password_here',
    client=new_client
)

print("Mapping the user to a workspace")
wu_map1 = UserWorkspaceMappingDetailModel.objects.create(
    workspace=new_workspace,
    user=new_user
)
print(wu_map1.__dict__)

print("Mapping the user to a workspace")
wu_map2 = UserWorkspaceMappingDetailModel.objects.create(
    workspace=new_workspace,
    user=new_user2
)
print(wu_map2.__dict__)

print("Mapping the user to a workspace")
wu_map3 = UserWorkspaceMappingDetailModel.objects.create(
    workspace=new_workspace2,
    user=new_user
)
print(wu_map3.__dict__)

# 2. Read Operations
print("Get All Users in a Workspace")
workspace_users = UserDetailModel.objects.filter(
    userworkspacemappingdetailmodel__workspace=new_workspace
)
print(workspace_users)

print("Get All Users in a Workspace 2")
workspace2_users = UserDetailModel.objects.filter(
    userworkspacemappingdetailmodel__workspace=new_workspace2
)
print(workspace2_users)

print("Get All Workspaces a User Belongs To")
user_workspaces = WorkspaceDetailModel.objects.filter(
    userworkspacemappingdetailmodel__user=new_user
)
print(user_workspaces)

print("Get All Users for a Client")
client_users = UserDetailModel.objects.filter(client=new_client)
print(client_users)
# 3. Update Operations

print("Add a User to Another Workspace")
# Assuming you have another workspace
another_workspace = WorkspaceDetailModel.objects.create(
    name='Secondary Workspace',
    client=new_client
)
print("workspace created")
print("Mapping the user to a workspace")

wu_map4 = UserWorkspaceMappingDetailModel.objects.create(
    workspace=another_workspace,
    user=new_user
)
print(wu_map4.__dict__)

print("Remove a User from a Workspace")
mapping = UserWorkspaceMappingDetailModel.objects.create(
    workspace=new_workspace,
    user=new_user
)
mapping.delete()

print("Update a Workspace Name")
print(new_workspace.name)
new_workspace.name = 'Very Main Workspace Name'
new_workspace.save()
print(new_workspace.name)

# 4. Delete Operations

print("Delete a User and Their Mappings")
user = UserDetailModel.objects.get(email='jane.doe@example.com')
print(user.name)
del_wu_map = UserWorkspaceMappingDetailModel.objects.get(user=user)
print(del_wu_map.__dict__)
print(user.delete())  # This will cascade and delete all related workspace mappings

print("Delete a Workspace and Cascade to Mappings")
# This will delete all related user mappings
workspace = WorkspaceDetailModel.objects.get(name='Very Main Workspace Name')
print(workspace)
del_wu_map = UserWorkspaceMappingDetailModel.objects.get(workspace=workspace)
print(del_wu_map.delete())
