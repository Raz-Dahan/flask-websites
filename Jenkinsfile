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
                script {
                    env.instance_id = $(aws ec2 describe-instances --filters "Name=tag:platform,Values=test" --query "Reservations[].Instances[].InstanceId" --output text)
                }
                sh 'echo "Testing..."'

                // Move tar file from S3 to EC2 instance with tag "platform:test"
                sh 'echo "Moving tar file to EC2..."'
                // sh 'instance_id=$(aws ec2 describe-instances --filters "Name=tag:platform,Values=test" --query "Reservations[].Instances[].InstanceId" --output text)'
                sh 'echo $instance_id'
                sh 'aws ec2 scp ~/alpaca.tar.gz ${instance_id}:~/alpaca.tar.gz'

                // Connect to the EC2 instance
                sh 'echo "Connecting to EC2..."'
                sh 'ssh -o StrictHostKeyChecking=no -i ~/.ssh/raz-key.pem ec2-user@${instance_id} "tar -xzvf ~/alpaca.tar.gz -C /home/ec2-user/"'

                // Optionally, you can run additional test commands here

                // Clean up the tar file on the EC2 instance
                sh 'echo "Cleaning up..."'
                sh 'ssh -o StrictHostKeyChecking=no -i ~/.ssh/raz-key.pem ec2-user@${instance_id} "rm ~/alpaca.tar.gz"'
            }
        }
    }
}
