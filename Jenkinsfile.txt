pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/shubhamdhiman200021/Demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 80:80 devops-app'
            }
        }

    }
}