def writeConfig(**kwargs):
    template = """
    apiVersion: v1
    kind: pod
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
            - containerPort: 80"""

    with open('somefile.yaml', 'w') as yfile:
        yfile.write(template.format(**kwargs))