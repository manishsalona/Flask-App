pipeline {
    agent any

    environment {
        DEPLOY_DIR = "/home/ubuntu/FlaskAPP"
        GIT_REPO = "https://github.com/manishsalona/Flask-App.git"
        STAGING_SERVER = "65.0.205.55"
        CREDENTIALS_ID = "Flask-Project" // Ensure this matches the ID in Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: "${env.GIT_REPO}"
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                    sudo apt-get update
                    sudo apt-get install -y python3-venv
                    '''
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh '''
                    . venv/bin/activate
                    pytest
                    '''
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: "${env.CREDENTIALS_ID}", keyFileVariable: 'SSH_KEY', usernameVariable: 'SSH_USER')]) {
                        sh """
                        scp -o StrictHostKeyChecking=no -i ${SSH_KEY} -r * ${SSH_USER}@${env.STAGING_SERVER}:${env.DEPLOY_DIR}
                        ssh -o StrictHostKeyChecking=no -i ${SSH_KEY} ${SSH_USER}@${env.STAGING_SERVER} <<EOF
cd ${DEPLOY_DIR}
. venv/bin/activate
pip install -r requirements.txt
nohup python3 app.py > flaskapp.log 2>&1 &
EOF
                        """
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                echo "Build completed with status: ${currentBuild.result}"
            }
        }
    }
}
