pipeline {
 environment {
    BACKUP_FOLDER = 'backups'
 }
  agent any

  stages {
    stage ('unit tests') {
        steps {
            echo "Running unit tests:"
        }
    }
    stage ('behat tests') {

      steps {
        sh "python3 --version;\
        python3 Builder.py"
      }
    }
  }
}