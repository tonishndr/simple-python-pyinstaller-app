node {
    def renderToken = 'your_ssh_key_here' // Ganti dengan kunci SSH Anda
    
    stage('Install Render CLI') {
        steps {
            sh 'curl -O https://render.com/static/cli/render/linux/render'
            sh 'chmod +x render'
            sh 'mv render /usr/local/bin/'
        }
    }
    
    stage('Build') {
        steps {
            checkout scm
            sh 'python -m py_compile sources/add2vals.py sources/calc.py'
        }
    }
    
    stage('Test') {
        steps {
            checkout scm
            sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            junit 'test-reports/results.xml'
        }
    }

    stage('Manual Approval') {
        steps {
            input message: 'Lanjutkan ke tahap Deploy'
        }
    }
    
    stage('Deploy') {
        steps {
            checkout scm
            sh 'pip install pyinstaller'  // Install pyinstaller
            sh 'pyinstaller --onefile sources/add2vals.py'
            archiveArtifacts artifacts: 'dist/add2vals', followSymlinks: false
            sh 'sleep 60'
            sh "ssh-add - <<< \"$renderToken\"" // Menambahkan kunci SSH ke agent
            sh 'render up --name my-app --path sources --docker my-docker-image'  // Deploy the app
        }
    }
}
