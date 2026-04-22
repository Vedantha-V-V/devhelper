# Lab 5: Prometheus and Grafana

## Step 1: Prepare Project Workspace
### Dashboard Task
1. Open your code editor and create a new folder named flask-container-lab.
2. Create files named main.py, requirements.txt, and Dockerfile.
3. Keep your Docker Desktop dashboard open to monitor images and containers.

### Commands
```bash
mkdir flask-container-lab
cd flask-container-lab
```

## Step 2: Create Flask App and Dependencies
### Dashboard Task
1. Add a minimal Flask app in main.py.
2. Add flask in requirements.txt.
3. Verify file list in editor side panel.

### Commands
```bash
cat > main.py << 'EOF'
from flask import Flask

app = Flask(__name__)

@app.route('/')
def health():
    return {'status': 'ok', 'service': 'flask-container-lab'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
EOF

cat > requirements.txt << 'EOF'
flask==3.1.0
EOF
```

## Step 3: Build and Run Docker Image
### Dashboard Task
1. In Docker Desktop, confirm new image appears after build.
2. Open container details and verify port mapping 5000.

### Commands
```bash
cat > Dockerfile << 'EOF'
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "main.py"]
EOF

docker build -t <dockerhub-username>/flask-container-lab:v1 .
docker run --name flask-lab -d -p 5000:5000 <dockerhub-username>/flask-container-lab:v1
docker ps
curl http://localhost:5000/
```

## Step 4: Push to Docker Hub
### Dashboard Task
1. Open Docker Hub and create repository flask-container-lab if needed.
2. Confirm the v1 tag appears in repository tags.

### Commands
```bash
docker login
docker push <dockerhub-username>/flask-container-lab:v1
```
