# Create Jenkins in local and attach volume to get persistant volume storage/

REF : https://rangle.io/blog/running-jenkins-and-persisting-state-locally-using-docker-2/
Jenkins docs : https://www.jenkins.io/doc/book/system-administration/viewing-logs/


Steps:

STEP 1 : 
- Pull Jenkins docker image - docker image pull jenkins/jenkins:lts

STEP 2 : 
- Create volume : docker volume create jenkins-volume
  jenkins-volume

STEP 3 :  
- Start the Jenkins container :
  > docker container run -d \
  -p 9090:8080 \
  -v jenkins-volume:/var/jenkins_home \
  --name jenkins-local \
  jenkins/jenkins:lts
 
OPTIONS EXPLAINED : 

-p for port mapping , host/ container
-v for previously created volume.
--name container name.

docker ps to get list of running containers,

STEP 4 :
Get the default password of Jenkins : 
 Since its jenkins docker container we've to ssh into it using exec commmand

> docker container exec \
0e40a54199f1 \
sh -c "cat /var/jenkins_home/secrets/initialAdminPassword"

here 0e40a54199f1 is my jenkins container Id, get from docker ps

STEP 5 : 
Jenkins URL : http://localhost:9090/

Testing the Persistent storage : 
 -
First, run 
> docker container kill [CONTAINER ID] 

to stop the instance. After doing so, run 

> docker container rm [CONTAINER ID] 

to completely remove the container instance.



