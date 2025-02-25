## Table of Contents

  - [Kubernetes Commands](#kubernetes-commands)
    - [Cluster Management](#cluster-management)
    - [Deployment Management](#deployment-management)
    - [Pod Management](#pod-management)
    - [Service Management](#service-management)
    - [Ingress Management](#ingress-management)
    - [Configuration Management](#configuration-management)
    - [Secret Management](#secret-management)
  - [Installation of minikube](#installation-of-minikube)
    - [Step 1: Install Dependencies](#step-1:-install-dependencies)
    - [Step 2: Install Kubectl](#step-2:-install-kubectl)
    - [Step 3: Download and Install Minikube](#step-3:-download-and-install-minikube)
    - [Step 4: Start Minikube](#step-4:-start-minikube)
    - [Step 5: Verify Minikube Cluster](#step-5:-verify-minikube-cluster)
    - [Start Minikube with a Master and a Worker Node](#start-minikube-with-a-master-and-a-worker-node)


## Kubernetes Commands

### Cluster Management

- Create a cluster: `kubectl create cluster`
- Get cluster information: `kubectl cluster-info`
- List all clusters: `kubectl get clusters`
- Delete a cluster: `kubectl delete cluster <cluster-name>`

### Deployment Management

- Create a deployment: `kubectl create deployment <deployment-name> --image=<image-name>`
- Get deployment information: `kubectl get deployments`
- Scale a deployment: `kubectl scale deployment <deployment-name> --replicas=<replica-count>`
- Update a deployment: `kubectl set image deployment/<deployment-name> <container-name>=<new-image>`
- Delete a deployment: `kubectl delete deployment <deployment-name>`

### Pod Management

- Get pod information: `kubectl get pods`
- Describe a pod: `kubectl describe pod <pod-name>`
- Get logs from a pod: `kubectl logs <pod-name>`
- Execute a command in a pod: `kubectl exec -it <pod-name> -- <command>`

### Service Management

- Create a service: `kubectl create service <service-type> <service-name> --tcp=<port>:<target-port>`
- Get service information: `kubectl get services`
- Describe a service: `kubectl describe service <service-name>`
- Delete a service: `kubectl delete service <service-name>`

### Ingress Management

- Create an ingress: `kubectl create ingress <ingress-name> --rule=<host>/<path>=<service-name>:<service-port>`
- Get ingress information: `kubectl get ingress`
- Describe an ingress: `kubectl describe ingress <ingress-name>`
- Delete an ingress: `kubectl delete ingress <ingress-name>`

### Configuration Management

- Create a config map: `kubectl create configmap <configmap-name> --from-file=<path-to-file>`
- Get config map information: `kubectl get configmaps`
- Describe a config map: `kubectl describe configmap <configmap-name>`
- Delete a config map: `kubectl delete configmap <configmap-name>`

### Secret Management

- Create a secret: `kubectl create secret generic <secret-name> --from-literal=<key>=<value>`
- Get secret information: `kubectl get secrets`
- Describe a secret: `kubectl describe secret <secret-name>`
- Delete a secret: `kubectl delete secret <secret-name>`


## Installation of minikube

### Step 1: Install Dependencies
Ensure your system has the necessary dependencies:
```bah
sudo apt update && sudo apt install -y curl wget apt-transport-https conntrack
```
### Step 2: Install Kubectl
- Minikube requires kubectl to interact with the cluster.
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```
- Verify the installation:
```bash
kubectl version --client
```
### Step 3: Download and Install Minikube
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
- Verify Minikube installation:
```bash
minikube version
```
### Step 4: Start Minikube
- Now, start Minikube using a supported driver (like Docker):
```bash
minikube start --driver=docker
```
- If you don't have Docker installed, you can install it using:
```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
```
- If you get any error like the following one:
```bash
Exiting due to PROVIDER_DOCKER_NEWGRP: "docker version --format <no value>-<no value>:<no value>" exit status 1: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.45/version": dial unix /var/run/docker.sock: connect: permission denied
```
Run the following command to add your user to the docker group:
```bash
sudo usermod -aG docker $USER
newgrp docker
```
- Then restart Minikube:
```bash
minikube delete
minikube start --driver=docker
```
### Step 5: Verify Minikube Cluster
- Check the cluster status:
```bash
kubectl get nodes
```
- Stop Minikube:
```bash
minikube stop
```
- Delete Minikube cluster:
```bash
minikube delete
```
- Access Minikube dashboard:
```bash
minikube dashboard
```
### Start Minikube with a Master and a Worker Node
Run the following command:
```bash
minikube start --nodes 2 --driver=docker
```
- --nodes 2 → Creates one master and one worker.
- --driver=docker → Uses Docker as the container runtime.