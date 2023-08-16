node {
    def renderToken = 'rnd_gZYFOScAftJVbFZsOlXjQINqYM5l'
    
    stage('Build') {
        // Check out the source code from Git
        checkout scm
        
        // Build stage using a Python 3 Docker container (note the change to Python 3)
        withDockerContainer(image: 'python:3') {
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
    
    stage('Deploy') {
        // Check out the source code from Git
        checkout scm

        // Run Deliver stage using a python:3 Docker container (note the change to Python 3)
        def deliverContainer = docker.image('python:3').inside("--user=root") {
            checkout scm
            sh 'pip install pyinstaller'  // Install pyinstaller
            sh 'pyinstaller --onefile sources/add2vals.py'
            archiveArtifacts artifacts: 'dist/add2vals', followSymlinks: false
            sh "docker login rendercr.io -u _json_key -p '$renderToken'"
            sh 'docker push my-app'  // Push the Docker image to Render's registry
            sh "render up my-app --path sources --docker"  // Deploy the app
        }
    }
}