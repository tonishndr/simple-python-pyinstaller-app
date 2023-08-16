node {
    def renderToken = 'rnd_gZYFOScAftJVbFZsOlXjQINqYM5l'

    stage('Build') {
        // Check out the source code from Git
        checkout scm
        
        // Build stage using a Python 2 Docker container
        withDockerContainer(image: 'python:2-alpine') {
            sh 'python -m py_compile sources/add2vals.py sources/calc.py'
        }
    }
    
    stage('Test') {
        // Check out the source code from Git
        checkout scm
        
        // Run tests using a qnib/pytest Docker container
        withDockerContainer(image: 'qnib/pytest') {
            sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            junit 'test-reports/results.xml'
        }
    }

    stage('Manual Approval') {
        input message: 'Lanjutkan ke tahap Deploy'
    }
    
    stage('Deploy to Render') {
        // def renderCli = docker.image('render/vercel:latest')
        
        renderCli.inside {
            sh "render login $renderToken"
            sh 'render up --name my-app --path sources --docker'
            sh 'sleep 60'
        }
    }
}