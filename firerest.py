from fireREST import Client

client = Client(hostname='192.168.0.239', username='admin', password='Firetruck1!')

net_obj = { 
    'name': 'NetObjViaAPI',
    'value': '198.18.1.0/24',
}

response = client.create_object('networks', net_obj)
