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
    
    stage('Deliver') {
        // Check out the source code from Git
        checkout scm
        
        // Build the executable using pyinstaller in a cdrx/pyinstaller-linux:python2 Docker container
        withDockerContainer(image: 'cdrx/pyinstaller-linux:python2') {
            sh 'pyinstaller --onefile sources/add2vals.py'
            archiveArtifacts artifacts: 'dist/add2vals'
        }
    }
}
