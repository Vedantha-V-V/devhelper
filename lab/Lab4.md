# Lab 4: Jenkins

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

## Step 1: Start Jenkins Service
### Dashboard Task
1. Create pipeline in the jenkins dashboard
2. Run the pipeline
3. Create a freestyle job
4. Archive the artifact 
5. Run the artifact
6. Write pipeline name and select pipeline

### Commands
```bash
sudo systemctl start jenkins
```

## Step 2: Running Jenkins Pipelines

### Commands
```bash
# View pipeline at localhost:8080
pipeline {
    agent any

    stages {
        stage('Check Python'){
            steps {
                sh 'python3 --version'
            }
        }

        stage('Build'){
            steps {
                git branch: 'master'
                    url: 'https://github.com/SANDHYAGOPAL/devops26lab.git'
                    sh 'python3 demo.py > output.txt'
            }
        }

        stage('Archive'){
            steps {
                archiveArtifacts artifacts: 'output.txt'
            }
        }

        stage('Deploy/Use'){
            steps {
                sh 'date'
                sh 'cat output.txt' 
            }
        }
    }
}
```
## Step 3: Saving Jenkins Artefact
### Dashboard Task
1. Save and build