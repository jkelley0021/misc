from fireREST import Client

client = Client(hostname='192.168.0.239', username='api-user', password='Firetruck1!')

name = 'NetObjViaAPI-3'
uuid = client.get_object_id_by_name('networks', name)
