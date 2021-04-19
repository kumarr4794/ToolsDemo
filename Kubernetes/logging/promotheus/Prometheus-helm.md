# Setup Prometheus Monitoring on Kubernetes using Helm and Prometheus Operator.

Operator link : https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack

# Install prometheus repo : 

`helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
`helm repo add stable https://kubernetes-charts.storage.googleapis.com/`
`helm repo update`

# Install prometheus chart : 
`helm install prometheus prometheus-community/kube-prometheus-stack`


# Install prometheus fixed version : 
`helm install prometheus prometheus-community/kube-prometheus-stack --version "9.4.1"`