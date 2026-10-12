
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'attagetto/praktikum-simple'
        REGISTRY_CREDENTIALS = 'dockerhub-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Melakukan checkout dari SCM...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Mulai build aplikasi'
                bat 'echo Build selesai'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Membangun Docker image...'
                bat '''
                    docker version
                    docker build -t "%IMAGE_NAME%:%BUILD_NUMBER%" -t "%IMAGE_NAME%:latest" .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKERHUB_USERNAME',
                        passwordVariable: 'DOCKERHUB_PASSWORD'
                    )
                ]) {
                    bat '''
                        @echo off
                        echo %DOCKERHUB_PASSWORD% | docker login -u %DOCKERHUB_USERNAME% --password-stdin
                        if errorlevel 1 exit /b 1

                        docker push "%IMAGE_NAME%:%BUILD_NUMBER%"
                        if errorlevel 1 exit /b 1

                        docker push "%IMAGE_NAME%:latest"
                        if errorlevel 1 exit /b 1

                        docker logout
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Selesai build!'
        }
    }
}
