# Lab 1: Docker Basics

## Step 1: Check existing docker images

### Commands
```bash
sudo su - 
docker images
```

## Step 2: Run existing docker images

### Commands
```bash
docker run hello-world
```

## Step 3: Pull Docker Image from Docker Hub

### Commands
```bash
docker pull nginx
```

## Step 4: Run docker image as a container

### Commands
```bash
docker run -d -p 8000:80 nginx
```

## Step 5: Check container ID
 
### Commands
```bash
docker ps
```


## Step 6: Stop the container

### Commands
```bash
docker stop [container_id]
```


## Step 7: Start the container

### Commands
```bash
docker start [image_name]
```

## Step 8: Delete the container

### Commands
```bash
docker rm container_id
```

## Step 9: Execution inside the Docker Container

### Commands
```bash
docker exec -it my-nginx-bash
```

## Step 10: Change contents of default nginx page

### Commands
```bash
cd /usr/share/nginz/html
```

## Step 11: Exit

### Commands
```bash
exit
```

## Step 12: Stop and Delete

### Commands
```bash
docker stop [container_id]
docker rm [container_id]
docker rmi [image_id]
```

