# Lab 3: Push Image to Docker Hub

## Step 1: Creating python server

### Commands
```bash
cd Documents
mkdir python-project
cd python-project

nano app.py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home_page(name=None):
    return render_template("index.html",name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

pip --version
sudo apt install python3-pip
pip install flask
python3 app.py
```

## Step 2: Creating docker image

### Commands
```bash
cd Documents
cd python-project
ls
nano Dockerfile

FROM python:3-alpine3.15
WORKDIR /app
COPY ./app

RUN pip install flask

CMD ["python3","app.py"]

# Docker build
sudo docker build -t pyimage:1 .

# List all docker images
sudo docker images

# Docker run
sudo docker run -p 8000:5000 pyimage:1

# Check port 8080
```

# Step 3: Push image to docker hub
### Dashboard Tasks
1. Open Docker Hub and create repository flask-container-lab if needed.
2. Confirm the v1 tag appears in repository tags.

### Commands
```bash
# Rename docker image
sudo docker image
sudo docker tag pyimage:1 vedanthavv/dockerimage

# Login
sudo docker login -u vedanthavv
sudo docker push vedanthavv/pyimage

# Logout
docker logout
```
