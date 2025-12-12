pipeline {
    agent {
        docker { 
            image 'jenkins-ci-agent' 
            args '-v /var/run/docker.sock:/var/run/docker.sock' 
        }
    }

    environment {
        SONAR_SCANNER_HOME = tool 'SonarScanner' // Sonar Scanner встановлено у Jenkins
        SONAR_URL = 'http://sonarqube:9000' //внутрішнє ім'я сервісу Compose

        // Змінні для Docker
        DOCKER_IMAGE = "vertex_app:${env.BUILD_ID}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/xarexw/vertex_app' // Ваш репозиторій
            }
        }
        
        stage('Run Tests') {
            steps {
                //юніт-тести
                sh 'docker compose run web python manage.py test' 
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv(credentialsId: 'SONAR_TOKEN', installationName: 'SonarQube') { // токен у Jenkins
                    sh "${SONAR_SCANNER_HOME}/bin/sonar-scanner -Dsonar.projectKey=vertex_app -Dsonar.sources=."
                }
            }
        }

        stage('Build and Deploy') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ." 
            
                    sh "docker compose up -d web" 
                }
            }
        }
    }
}