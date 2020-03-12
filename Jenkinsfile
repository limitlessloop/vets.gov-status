pipeline {
  agent {
    label 'vetsgov-general-purpose'
  }

  stages {
    stage('Unit tests') {
      steps {
        script {
          sh './run-ci-tests.sh'  // this copies results into ./results directory
        }
      }
      post {
        always {
          junit testResults: 'results/unit/pytest-unit.xml'
        }
        success {
          archiveArtifacts artifacts: "results/coverage/**"
          publishHTML(target: [reportDir: 'results/coverage', reportFiles: 'index.html', reportName: 'Coverage', keepAll: true])
        }
      }
    }
    stage('Build') {
      steps {
        script {
          // slackSend message: "Scorecard Jenkins build started", color: "good", channel: "scorecard-ci-temp"
          sh 'cd src && yarn install --frozen-lockfile --production=true'
          dockerImage = docker.image('jekyll/jekyll:4.0')
          args = "--volume=${pwd()}:/srv/jekyll"

          dockerImage.inside(args) {
              sh '/usr/gem/bin/jekyll build --trace'
          }
        }
      }
    }

    stage('Upload') {
      when {
        expression {
          (env.BRANCH_NAME == 'demo' ||
          env.BRANCH_NAME == 'master' ||
          env.BRANCH_NAME == 'production') &&
          !env.CHANGE_TARGET
        }
      }
      steps {
        script {
          slackSend message: "Scorecard Jenkins upload started", color: "good", channel: "scorecard-ci-temp"
          def envs = [
            'demo': ['dev'],
            'master': ['staging'],
            'production': ['prod'],
          ]

          for (e in envs.get(env.BRANCH_NAME, [])) {
            sh "bash --login -c 'aws s3 sync --acl public-read --delete --region us-gov-west-1 _site s3://dsva-vetsgov-scorecard-${e}/'"
          }
        }
      }
    }
  }
  post {
    always {
      deleteDir() /* clean up our workspace */
    }
    success {
      echo "Build success"
      // slackSend message: "Scorecard Jenkins build succeeded", color: "good", channel: "scorecard-ci-temp"
    }
    failure {
      echo "Build failure"
      // slackSend message: "Scorecard Jenkins build *FAILED*!", color: "danger", channel: "scorecard-ci-temp"
    }
  }
}
