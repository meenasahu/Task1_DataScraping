import requests

purl='https://httpbin.org/post'

pHeaders={
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'user-name' : "['vigo','Tech']"
     }

dresp=requests.post(url=purl,headers=pHeaders)

jresp=dresp.json()

print('dresp.content',jresp['headers'])