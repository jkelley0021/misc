from fireREST import Client

client = Client(hostname='192.168.0.239', username='api-user', password='Firetruck1!')

net_obj = {
    'name': 'server-9',
    'value': '9.9.9.9',
}

response = client.create_object('hosts', net_obj)
