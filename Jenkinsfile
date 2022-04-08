pipeline{
    agent any
    environment{
        
        registry = "Benson700/https://github.com/benson700/DevOps-Core-Practical-Project.git" 
        registryCredential = 'dockerhub_id' 
        dockerImage = '' 
    }
    stages{
        stage('Unit Testing'){
            steps{ 
                apt install python3.8-venv
                sh "bash scripts/test.sh"
            }
        }   
        stage('Build Images'){
            steps{
                sh "bash scripts/build.sh"
            }
        }
        stage('Push Images'){
            steps{
                sh "bash scripts/push.sh"
            }
        }
        stage('Configure & Deploy'){
            steps{
                sh "bash scripts/deploy.sh"
            
            }
        }
    }
}