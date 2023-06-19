pipeline {
    agent any
    environment {
        EC2_IP = "18.196.60.253"
    }
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
                sh 'ssh -o StrictHostKeyChecking=no -i /var/lib/jenkins/raz-key.pem ec2-user@${EC2_IP}'
                withAWS(credentials: 'aws_admins') {
                sh 'aws s3 cp s3://raz-flask-artifacts/alpaca.tar.gz /var/lib/jenkins/workspace/alpaca.tar.gz'
                sshagent(['ssh-config']) {
                         sh 'scp -i /var/lib/jenkins/raz-key.pem /var/lib/jenkins/workspace/crypto.tar.gz ec2-user@${EC2_IP}:/home/ec2-user'
                    }
                }
            }
        }
    }
}
