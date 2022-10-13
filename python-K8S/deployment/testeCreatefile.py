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

with open('deployment-nginx.yaml', 'w') as yfile:
        yfile.write(template.format())