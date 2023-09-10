# This is a test repo to learn CICD and orchestration

:bangbang: __Disclaimer: This repo is not a depiction of my skillset. There may be incorrect explanation or code inside it as I've just started learning it__ :grin:

## 1. Using kubernetes
To run it with kubernetes, you need minikube and docker. To do successful deployment you need to run the following commands, in a new terminal.
1. `minikube delete`
2. `minikube start`
3. `eval $(minikube -p minikube docker-env)`
4. `docker-compose build --no-cache`
5. `kubectl -f apply kubernetes/service.yaml`
6. `kubectl -f apply kubernetes/deployment.yaml`

Then to expose this, do `minikube service <service-name>`


## 2. Using standalone docker
In a new terminal do
1. `docker-compose build --no-cache`
2. `docker-compose up -d`

To kill it, do `docker-compose down`