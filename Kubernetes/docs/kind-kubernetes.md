# How to create single/multi node K8s cluster in local.

Guide: https://kind.sigs.k8s.io/

###Mac: 
> brew install kind

###Creating a Cluster: 
> kind create cluster

To specify another image use the 
   `--image flag – kind create cluster --image=...`

To Build custom image: 
https://kind.sigs.k8s.io/docs/user/quick-start/#building-images

Help : kind create cluster --help

### Deleting a Cluster:
>kind delete cluster 