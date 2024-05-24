Caso prefira o minikube é possivel utilizar o podman junto com o minikube.
```
minikube config set driver podman

minikube start --driver=hyperkit
```

kubectl get all

# Acessar um serviço utilizando minikube URL
```
kubectl create deployment --image=nginx nginx --replicas=4
kubectl expose deployment nginx --type=LoadBalancer --port=80
kubectl get svc
minikube service nginx --url
curl http://192.168.205.4:31385
```