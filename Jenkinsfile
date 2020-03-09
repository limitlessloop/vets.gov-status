pipeline {
  agent {
    label 'vagov-general-purpose'
  }

  stages {
    stage('Build') {
      steps {
        script {
          slackSend message: "Scorecard Jenkins build started", color: "good", channel: "va-scorecard-refresh"
          dockerImage = docker.image('jekyll/jekyll:4.0')
          args = "-v ${pwd()}:/srv/jekyll"
          dockerImage.inside(args) {
            sh '/usr/gem/bin/jekyll build'
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
          slackSend message: "Scorecard Jenkins upload started", color: "good", channel: "va-scorecard-refresh"
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
      slackSend message: "Scorecard Jenkins build succeeded", color: "good", channel: "va-scorecard-refresh"
    }
    failure {
      slackSend message: "Scorecard Jenkins build *FAILED*!", color: "danger", channel: "va-scorecard-refresh"
    }
  }
}
