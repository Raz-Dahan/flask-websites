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
                sh 'echo "Building..."'
                sh 'git clone https://github.com/Raz-Dahan/sample-flask.git'
                sh 'ls'
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Building..."'
                sh 'echo "packaging"'
                sh 'tar -czvf alpaca.tar.gz sample-flask'
                sh 'ls'
            }
        }
        stage('Push To Cloud') {
            steps {
                sh 'echo "pushing to s3"'
                sh 'echo "packaging"'
                sh 'aws s3 cp alpaca.tar.gz s3://raz-pipeline-test'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Testing..."'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying..."'
            }
        }
    }
}