# Kubernetes local

Utilizar o kubernetes local com podman e kind.

Em alguns casos não é possivel utilizar o docker localmente.

Para estes casos podemos levantar uma máquina com podman e utilizar containers podman para o cluster kind.
![Maiores detalhes aqui](/kind/commands.txt)




Caso prefira o minikube é possivel utilizar o podman junto com o minikube.
```
minikube config set driver podman

minikube start --driver=hyperkit
```
