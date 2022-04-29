import http.client

from config import API_TOKEN as jwt

header = {'Authorization': f'Bearer {jwt}',
          'Content-Type': 'application/json',
          'Accept': 'application/json'}

ani = http.client.HTTPSConnection('api.aniapi.com')
ani.request('GET', '/v1/auth/me', headers=header)
res = ani.getresponse()
readed = res.read()
print(readed.decode('utf-8'))
