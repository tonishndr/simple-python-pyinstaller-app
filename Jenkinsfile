node {
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
        input message: 'Lanjutkan ke tahap Deploy ?'
    }
    
    stage('Deploy') {
        // Check out the source code from Git
        checkout scm

        // Run Deliver stage using a cdrx/pyinstaller-linux:python2 Docker container
        def deliverContainer = docker.image('python:3').inside("--user=root") {
        checkout scm
        sh 'pip install pyinstaller'  // Install pyinstaller
        sh 'pyinstaller --onefile sources/add2vals.py'
        archiveArtifacts artifacts: 'dist/add2vals', followSymlinks: false
        sh 'sleep 60'
        }
    }
}
