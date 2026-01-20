pipeline {
    agent any

    tools {
        maven 'Maven'
        jdk 'Java'
    }

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/PoojaPrakash08/git-fetch-pull-demo.git'
            }
        }

        stage('Maven Build') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('Deploy to Tomcat') {
            steps {
                sh '''
                cp target/*.war /opt/tomcat/webapps/
                '''
            }
        }
    }
}
