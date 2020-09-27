from fireREST import Client

client = Client(hostname='192.168.0.239', username='api-user', password='Firetruck1!')

{
net_obj = { 
    'name': 'NetObjViaAPI-1',
    'value': '198.18.1.0/24',
},
net_obj = { 
    'name': 'NetObjViaAPI-2',
    'value': '198.18.2.0/24',
},
net_obj = { 
    'name': 'NetObjViaAPI-3',
    'value': '198.18.3.0/24',
}
}
response = client.create_object('networks', net_obj)
