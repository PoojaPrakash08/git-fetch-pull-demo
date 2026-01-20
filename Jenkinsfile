pipeline {
    agent any

    tools {
        maven 'Maven-3.9.1' // Replace with your Maven installation name in Jenkins
        jdk 'Java-17'       // Replace with your JDK installation name
    }

    environment {
        TOMCAT_USER = 'admin'           // Tomcat admin username
        TOMCAT_PASS = 'admin-password'  // Tomcat admin password
        TOMCAT_URL  = 'http://localhost:8080/manager/text'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/PoojaPrakash08/git-fetch-pull-demo.git'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('Deploy') {
            steps {
                deploy adapters: [tomcat9(
                    credentialsId: 'tomcat-cred', 
                    url: "${TOMCAT_URL}"
                )], contextPath: '/myapp', war: '**/target/*.war'
            }
        }
    }
}
