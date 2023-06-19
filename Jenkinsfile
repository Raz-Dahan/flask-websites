pipeline {
    agent any
    stages {
        stage('Cleanup') {
            steps {
                sh 'echo "Performing cleanup..."'
                sh 'rm -rf *'
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Building..."'
                sh 'git clone https://github.com/Raz-Dahan/sample-flask.git'
                sh 'echo "Packaging..."'
                sh 'tar -czvf alpaca.tar.gz sample-flask'
                sh 'ls'
            }
        }
        stage('Push To Cloud') {
            steps {
                sh 'echo "Pushing to S3..."'
                sh 'echo "Packaging..."'
                sh 'aws s3 cp alpaca.tar.gz s3://raz-flask-artifacts'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Testing..."'

                // Move tar file from S3 to EC2 instance
                sh 'echo "Moving tar file to EC2..."'
                sh 'aws s3 cp s3://raz-flask-artifacts/alpaca.tar.gz ~/alpaca.tar.gz'

                // Extract tar file on EC2 instance
                sh 'echo "Extracting tar file..."'
                sh 'tar -xzvf ~/alpaca.tar.gz -C /home/ec2-user/'

                // Optionally, you can run additional test commands here

                // Clean up the tar file on EC2 instance
                sh 'echo "Cleaning up..."'
                sh 'rm ~/alpaca.tar.gz'
            }
        }
    }
}
