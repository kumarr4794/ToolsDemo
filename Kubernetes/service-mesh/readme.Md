# What is service Mesh ?
    Service Mesh manages communication between microservices.

Why we need dedicated tool to maintain this?

Intro of Microservices introduced problem, An app can have multiple services. When services needs to talk to talk/communication.
    - Backend logic.
    - New endpoint is added thats need to added in other pods/server too.
    - Comm within cluster is not available.
    - Add retry logics to service.
    - Monitoring.

Devs busy adding logic like network


So service mesh is answers this above problem.

Pod with sidecar proxy, with above logics and service mesh injects all this data.

Traffic Split config: 

Having diff version of code and testing it individual by sending certain percentage of traffic [canary deployment]

# ISTIO is Implementation of Service Mesh.

Istiod : Control Plane and contains [Pilot , Citadel , Galley ] config,discovery,certificates.

Proxy : Envoy Proxy which is injected into each pod/microservice as sidecar.

CRDs :

Virtual Service : How to route your traffic to a given destination.

DestinationRule : configures what happens to traffic FOR that destination.

We configure only control plane, not proxies.

How Service Discovery,sercurity,metrics works :

Dynamic Service Discovery:  Istiod hasCentral registry in Istiod using service registries envoy works/functions.

Citadel : generates CA for TLS comms

Metrics


Istio Ingress Gateway : An Entry point to K8s alternative to ngnix ingress controller acts as loadbalancer. It directs traffic to one of pod using Virtual service components.

Cluster Req -------> Ingress Gateway.

###### Important ###########

Create a Istio Gatewaty using `kind: Gateway` component,

configure Routes for traffic entering via Gateway using `kind: VirtualService`



Traffic Flow into K8s : 

- Users initate req --> Istio Gateway [Intercepts]. 
- Its evaluates req and routes based on VS --> Envoy Proxy
- Envoy-> Service
