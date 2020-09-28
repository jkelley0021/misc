from fireREST import Client

client = Client(hostname='192.168.0.239', username='api-user', password='Firetruck1!')

net_obj = { 
    'name': 'server-4',
    'value': '4.4.4.4',
}

response = client.create_object('hosts', net_obj)

net_obj = { 
    'name': 'server-5',
    'value': '5.5.5.5',
}

response = client.create_object('hosts', net_obj)
