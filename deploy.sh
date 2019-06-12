docker build -t gginis/multi-client:latest -t gginis/multi-client:$SHA -f ./client/Dockerfile ./client
docker build -t gginis/multi-server:latest -t gginis/multi-server:$SHA -f ./server/Dockerfile ./server
docker build -t gginis/multi-worker:latest -t gginis/multi-worker:$SHA -f ./worker/Dockerfile ./worker

docker push gginis/multi-client:latest
docker push gginis/multi-server:latest
docker push gginis/multi-worker:latest

docker push gginis/multi-client:$SHA
docker push gginis/multi-server:$SHA
docker push gginis/multi-worker:$SHA

kubectl apply -f k8s
kubectl set image deployments/client-deployment client=gginis/multi-client:$SHA
kubectl set image deployments/server-deployment server=gginis/multi-server:$SHA
kubectl set image deployments/worker-deployment worker=gginis/multi-worker:$SHA

