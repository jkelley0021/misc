from fireREST import Client

client = Client(hostname='192.168.0.239', username='api-user', password='Firetruck1!')

net_obj = { 
    'name': '{{  NetObjName  }}',
    'value': '{{  address  }}',
}

response = client.create_object('networks', net_obj)