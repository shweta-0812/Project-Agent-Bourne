from models.client_detail_model import ClientDetailModel

# 0. Clear slate
print("::::Delete a Client:::")
all_client = ClientDetailModel.objects.all().delete()
print(all_client)

# Create a new client record
# 1.Create a New Client
print("::::Create a new client record:::")

client = ClientDetailModel.objects.create(
    domain='example.com',
    name='Example Client',
    timezone='UTC'
)
print(client)

# 2.Read (Retrieve) a Client
#
print("::::Retrieve by UUID:::")
client = ClientDetailModel.objects.get(uuid=client.uuid)
print(client)

print("::::Retrieve by Domain:::")
client = ClientDetailModel.objects.get(domain='example.com')
print(client)

print("::::Retrieve All Clients:::")
clients = ClientDetailModel.objects.all()
print(client)

# 3. Update a Client
print("::::Update a Client:::")
client = ClientDetailModel.objects.get(domain='example.com')
client.name = 'Updated Client Name'
client.timezone = 'PST'
client.save()
print(client)

# 4. Delete a Client
print("::::Delete a Client:::")
all_client = ClientDetailModel.objects.all().delete()
print(all_client)
