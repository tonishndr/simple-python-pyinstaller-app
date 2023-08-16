pipeline {
    agent any
    
    stages {
        stage('Install Render CLI') {
            steps {
                sh 'curl -O https://render.com/static/cli/render/linux/render'
                sh 'chmod +x render'
                sh 'mkdir -p /var/jenkins_home/bin/'
                sh 'mv render /var/jenkins_home/bin/'
            }
        }
        
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                script {
                    // Build stage using a Python 2 Docker container
                    docker.image('python:2-alpine').inside {
                        sh 'python -m py_compile sources/add2vals.py sources/calc.py'
                    }
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    // Run tests using a qnib/pytest Docker container
                    docker.image('qnib/pytest').inside {
                        sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
                    }
                    junit 'test-reports/results.xml'
                }
            }
        }
        
        stage('Manual Approval') {
            steps {
                input message: 'Lanjutkan ke tahap Deploy'
            }
        }
        
        stage('Deliver') {
            when {
                expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
            }
            steps {
                script {
                    // Check out the source code from Git
                    checkout scm
                    
                    // Build the Docker image
                    def dockerImage = docker.build('my-docker-image', '.')
                    
                    // Run Deliver stage using a Docker container
                    def deliverContainer = docker.image('python:3').inside("--user=root") {
                        sh 'pip install pyinstaller'  // Install pyinstaller
                        sh 'pyinstaller --onefile sources/add2vals.py'
                        archiveArtifacts artifacts: 'dist/add2vals', followSymlinks: false
                        sh 'sleep 60'
                        sh 'render up --name my-app --path sources --docker my-docker-image'  // Deploy the app
                    }
                }
            }
        }
    }
}
