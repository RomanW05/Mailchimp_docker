pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RomanW05/Mailchimp_docker.git']])
            }
        }
        stage('Build') {
            steps {
                git 'https://github.com/RomanW05/Mailchimp_docker.git'
                sh 'docker build -t Mailchimp_docker .'
                sh 'docker run -it -p 80:80 --rm Mailchimp_docker'
            }
        }
        stage('Test') {
            steps {
                sh 'python3.11 -m pytest'
            }
        }
    }
}
