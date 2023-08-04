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

        // sh 'docker run --rm -v /var/jenkins_home/workspace/submission-cicd-pipeline-tonishnr/sources:/src cdrx/pyinstaller-linux:python2 \'pyinstaller -F add2vals.py\''
        // archiveArtifacts artifacts: 'sources/add2vals.py', followSymlinks: false
        // sh 'docker run --rm -v /var/jenkins_home/workspace/submission-cicd-pipeline-tonishndr/sources:/src cdrx/pyinstaller-linux:python2 \'rm -rf build dist\''
        // sleep time: 1, unit: 'MINUTES'
        
        // Run Deliver stage using a cdrx/pyinstaller-linux:python2 Docker container
        def deliverContainer = docker.image('cdrx/pyinstaller-linux:python2').inside("--user=root") {
        checkout scm
        sh 'pip install pyinstaller'  // Install pyinstaller
        sh 'pyinstaller --onefile sources/add2vals.py'
        archiveArtifacts artifacts: 'dist/add2vals', followSymlinks: false
        }
    }
}
