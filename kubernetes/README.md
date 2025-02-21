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

