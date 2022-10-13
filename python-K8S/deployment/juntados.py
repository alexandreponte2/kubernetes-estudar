from os import path
import yaml
from kubernetes import client, config
template = """
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 10
  template:
    metadata:
      name: nginx-pod
      labels:
        app: nginx-pod
    spec:
      containers:
        - name: nginx-container
          image: nginx:stable
          ports:
            - containerPort: 80
  selector:
    matchLabels:
      app: nginx-pod"""

with open('somefile.yaml', 'w') as yfile:
        yfile.write(template.format())


config.load_kube_config()

with open(path.join(path.dirname(__file__), "somefile.yaml")) as f:
    dep = yaml.safe_load(f)
    k8s_apps_v1 = client.AppsV1Api()
    resp = k8s_apps_v1.create_namespaced_deployment(
        body=dep,
        namespace="default")
    print("Deployment created. status='%s'" % resp.metadata.name)

