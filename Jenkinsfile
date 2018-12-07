pipeline {
 environment {
    BACKUP_FOLDER = 'backups'
 }
  agent any

  stages {
    stage ('unit tests') {
        steps {
            sh "echo Running unit tests:"
        }
    }
    stage ('behat tests') {

      steps {
        sh "python3 --version"
      }
    }
  }
}