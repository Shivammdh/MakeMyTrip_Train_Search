pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Shivammdh/MakeMyTrip_Train_Search.git']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/Shivammdh/MakeMyTrip_Train_Search.git'
                
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m Tests.maintest'
            }
        }
    }
}
