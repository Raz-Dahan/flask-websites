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
                script {
                    try {
                        withAWSCLI(credentials: 'aws_admins') {
                            sh 'aws ec2 describe-instances --filters "Name=tag:platform,Values=test"'
                            // Perform other AWS CLI commands as needed
                        }
                        
                        def instances = awsEC2.describeInstances(
                            [
                                filters: [
                                    [name: 'tag:platform', values: 'test']
                                ]
                            ]
                        ).reservations.flatten().collectMany { it.instances }

                        if (instances.size() == 0) {
                            error("No instances found with the 'platform:test' tag.")
                        } else if (instances.size() > 1) {
                            error("Multiple instances found with the 'platform:test' tag. Please ensure only one instance has this tag.")
                        } else {
                            def instanceId = instances[0].instanceId
                            sh "aws s3 cp s3://raz-flask-artifacts/alpaca.tar.gz /home/ec2-user/"
                            sh "tar -xzvf /home/ec2-user/alpaca.tar.gz -C /home/ec2-user/"
                            // Perform other test-related tasks on the EC2 instance
                        }
                    } catch (Exception e) {
                        error("An error occurred during the 'Test' stage: ${e.getMessage()}")
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying..."'
            }
        }
    }
}
