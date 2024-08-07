import urllib.request as request
import json

with request.urlopen('https://my-json-server.typicode.com/Lockseed/vuemastery-real-world-vue-3/events') as f:
    data = f.read().decode('utf-8')
    print('Status:', f.status, f.reason)
    # for k, v in f.getheaders():
    #     print(f"{k}: {v}")
    print(json.loads(data))