pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RomanW05/MailChimp.git']])
            }
        }
        stage('Build') {
            steps {
                git 'https://github.com/RomanW05/MailChimp.git'
                sh 'docker build -t mailchimp .'
                sh 'docker run -it -p 80:80 --rm mailchimp'
            }
        }
        stage('Test') {
            steps {
                sh 'python3.11 -m pytest'
            }
        }
    }
}
