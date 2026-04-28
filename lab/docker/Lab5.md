# Lab 5: Prometheus and Grafana

## Step 1: Create Prometheus File
### Dashboard Tasks

### Commands
```bash
cd Documents
mkdir monitoring
cd monitoring
nano prometheus.yml

global:
    scrape_interval: 15s

scrape_configs:
 - job_name: "prometheus"
   static_configs:
    - targets: ["localhost:9090"]
```

## Step 2: Create Docker Compose File
### Dashboard Tasks

### Commands
```bash
nano docker-compose.yml

version: '3';

services:
 prometheus:
  image: prom/prometheus
  container_name: prometheus
  volumes:
  -./prometheus.yml:/etc/prometheus/prometheus.yml
ports:
- "9090:9090"

 grafana:
  image: grafana/grafana
  container_name: grafana
  ports:
   - "3000:3000"
```

## Step 3: Start Containers
### Dashboard Tasks
1. Open http://localhost:9090
2. Open http://localhost:3000

### Commands
```bash
sudo docker compose up -d
sudo docker compose down
```