from fireREST import Client

client = Client(hostname='192.168.0.239', username='api-user', password='Firetruck1!')


obj_name = 'NetObjViaAPI-2'
obj_id = client.get_object_id_by_name('network', 'NetObjViaAPI-2')
obj_payload = client.get_object('networks', obj_id).json
