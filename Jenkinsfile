pipeline {
    agent any
    
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Render CLI') {
            steps {
                sh '''
                    curl -O https://render.com/static/cli/render/linux/render
                    chmod +x render
                    mv render /var/jenkins_home/bin/
                '''
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t my-docker-image .'
            }
        }
        
        stage('Test') {
            steps {
                sh 'docker run my-docker-image python -m unittest discover tests'
            }
        }
        
        stage('Manual Approval') {
            steps {
                input message: 'Deploy to Production?'
            }
        }
        
        stage('Deliver') {
            steps {
                script {
                    def deliverContainer = docker.image('python:3').inside("--user=root") {
                        sh 'pip install render-python'
                        sh 'render deploy'
                    }
                }
            }
        }
    }
}
