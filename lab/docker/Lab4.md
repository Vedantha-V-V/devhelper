# Lab 4: Jenkins

## Step 1: Start Jenkins Service
### Dashboard Tasks
1. # Create pipeline in the jenkins dashboard
2. # Run the pipeline

### Commands
```bash
sudo systemctl start jenkins
```

## Step 2: Running Jenkins Pipelines
### Dashboard Tasks
1. Create a freestyle job
2. Archive the artifact 
3. Run the artifact
4. View pipeline at localhost:8080
5. Write pipeline name and select pipeline

### Commands
```bash
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

### Commands
```bash
```