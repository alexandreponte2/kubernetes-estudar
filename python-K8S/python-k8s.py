import os
import utils
import yaml

kubeconf = os.getenv('KUBECONFIG')
conf = utils.load_auto_config(kubeconf)
client = utils.setup_request(conf)

ret = client.get(f'{conf.url}/api/v1/namespaces')
assert ret.status_code == 200

for i in ret.json()['items']:
    print (i['metadata']['name'])

