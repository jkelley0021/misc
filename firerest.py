from fireREST import Client

client = Client(hostname='192.168.0.239', username='admin', password='Firetruck1!')

auth_session = {
  'X-auth-access-token': 'c26c28a0-c871-454f-b8e0-18c60c00562e',
  'X-auth-refresh-token': '9d381948-2fde-47d0-a28b-f4b0bb21fe81',
  'DOMAINS': '[{"name":"Global","uuid":"e276abec-e0f2-11e3-8169-6d9ed49b625f"}, {"name":"Global/Devel","uuid":"61e913a3-4bd6-7bde-54b6-000000000000"}]',
}
client = Client(hostname='fmc.example.com', session=auth_session)

net_obj = { 
    'name': 'NetObjViaAPI',
    'value': '198.18.1.0/24',
}

response = client.create_object('networks', net_obj)