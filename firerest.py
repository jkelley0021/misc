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

net_obj = {
    'name': 'server-6',
    'value': '6.6.6.6',
}

response = client.create_object('hosts', net_obj)

net_obj = {
    'name': 'server-7',
    'value': '7.7.7.7',
}

response = client.create_object('hosts', net_obj)

net_obj = {
    'name': 'server-8',
    'value': '8.8.8.8',
}

response = client.create_object('hosts', net_obj)

net_obj = {
    'name': 'server-9',
    'value': '9.9.9.9',
}

response = client.create_object('hosts', net_obj)
