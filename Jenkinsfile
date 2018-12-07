pipeline {
 environment {

 }
  agent any

  stages {
    stage ('unit tests') {
        echo "Running unit tests:"
    }
    stage ('behat tests') {

      steps {
        sh "python3 --version;\
        python3 Builder.py"
      }
    }
  }
}