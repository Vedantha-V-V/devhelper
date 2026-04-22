# Lab Template: Docker to Kubernetes Workflow

Use this template for new labs. Each step has two required parts:
- Dashboard Task: UI actions on any web dashboard or portal.
- Commands: terminal commands to execute.

## Step 1: [Name Your Step]
### Dashboard Task
1. Open [dashboard-url-here].
2. Navigate to [page-name].
3. Confirm [thing-you-should-see].

### Commands
```bash
# Add commands to run for Step 1
```

## Step 2: [Build or Pull Image]
### Dashboard Task
1. Open Docker Desktop or Docker Hub.
2. Verify repository [repo-name] exists.

### Commands
```bash
docker login
docker build -t <dockerhub-username>/<app-name>:v1 .
docker push <dockerhub-username>/<app-name>:v1
```

## Step 3: [Deploy to Kubernetes]
### Dashboard Task
1. Open your Kubernetes dashboard.
2. Select the target namespace.
3. Watch workload and service health.

### Commands
```bash
kubectl create deployment <app-name> --image=<dockerhub-username>/<app-name>:v1
kubectl expose deployment <app-name> --type=LoadBalancer --port=80 --target-port=80
kubectl get pods
kubectl get svc
```

## Step 4: [Validation and Cleanup]
### Dashboard Task
1. Verify the app is reachable from browser/API client.
2. Capture screenshots or notes in your dashboard.

### Commands
```bash
kubectl logs deployment/<app-name>
kubectl delete service <app-name>
kubectl delete deployment <app-name>
```
