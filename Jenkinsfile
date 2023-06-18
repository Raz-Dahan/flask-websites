pipeline {
    agent any
    stages {
        stage('Cleanup') {
            steps {
                // Perform the cleanup step here
                sh 'echo "Performing cleanup..."'
                sh 'rm -rf *'
            }
        }
        stage('Clone') {
            steps {
                // Perform the clone step here
                sh 'echo "Building..."'
                sh 'git clone https://github.com/Raz-Dahan/sample-flask.git'
                sh 'ls'
            }
        }
        stage('Build') {
            steps {
                // Perform the build step here
                sh 'echo "Building..."'
                sh 'echo "packaging"'
                sh 'tar -czvf alpaca.tar.gz sample-flask'
                sh 'ls'
            }
        }
        stage('Push To Cloud') {
            steps {
                // Perform the push to cloud step here
                sh 'echo "pushing to s3"'
                sh 'echo "packaging"'
                sh 'aws s3 cp alpaca.tar.gz s3://raz-pipeline-test'
            }
        }
        stage('Test') {
            steps {
                // Perform the test step here
                sh 'echo "Testing..."'
            }
        }
        stage('Deploy') {
            steps {
                // Perform the deploy step here
                sh 'echo "Deploying..."'
            }
        }
    }
}
