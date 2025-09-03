## Запуск нода 
```
minikube start --memory=4096 --cpus=2
```

## Собрать образ
```
docker build -t iris-model-app:latest .   
```

## Запушить образ
```
docker login
docker tag iris-model-app:latest artemgalliamov/iris-model
docker push artemgalliamov/iris-model-app:latest
```

## Для секретов
```
kubectl create secret docker-registry docker-hub-secret \ --docker-server=https://index.docker.io/v1/ \ --docker-username=YOUR_DOCKERHUB_USERNAME \ --docker-password=YOUR_DOCKERHUB_PASSWORD \ --docker-email=YOUR_EMAIL
```

## Всё поднимаем
```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl create serviceaccount iris-model
kubectl patch serviceaccount iris-model -p '{"imagePullSecrets": [{"name": "docker-hub-secret"}]}'
```

## Создать туннель к нашему сервису
```
kubectl port-forward service/iris-model-app 8080:80
```