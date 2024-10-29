import requests

purl='https://httpbin.org/patch'

pHeaders={
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'user-name' : "['vigo','Tech']"
     }

dresp=requests.patch(url=purl,headers=pHeaders)

jresp=dresp.json()

print('dresp.content',jresp['headers'])

respHeader=jresp['headers']

print('dresp.content',respHeader['User-Name'],'type= ',type(respHeader['User-Name']))


ConvertStringlist=respHeader['User-Name'].split()

print('dresp.content',respHeader['User-Name'],'type= ',type(ConvertStringlist))