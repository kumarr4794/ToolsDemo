Reference : https://prometheus.io/docs/introduction/overview/
Youtube The DevOps Guy : https://www.youtube.com/watch?v=5o37CGlNLr8&list=PLHq1uqvAteVuEXCrRkPFWLXRKWNLOVUHn
TechWorld Nana : https://www.youtube.com/watch?v=h4Sl21AKiDg

# What is Prometheus ??
 - Is a Monitoring tool , Capable of monitoring anything. Is an open-source systems monitoring and alerting tool by sonarcloud.

  Like  - Microservices
        - Infra, CICD
        - Servers [Linux and Windows]
        - Legacy servers,

It uses Pull Approach for monitoring. Lets say we have 3 services from above list and Prometheus scrapes the
Service endpoints for metrics. 

# How it works ? 
In Leymann terms we have to deploy an agent/deamon [node exporter] in respective service. And it creates a metrics endpoint in each one of the service ex. [http://host:port/metrics] , Install a linux machine with prometheus in a subnet and give a yaml with endpoints defined which needs to be scraped.

Federate Endpoint: Endpoint which other prometheus can scrape.

        
Service Monitor : Service discovery