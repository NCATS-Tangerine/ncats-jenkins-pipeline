pipeline {
	agent any

	environment {
		KGX_GIT='https://github.com/NCATS-tangerine/kgx.git'
		PYTHONPATH='$WORKSPACE/kgx'
	}
	options {
		// using the timestamps plugin we can add timestamps to the console log
		timestamps()
	}

	stages {
		stage('KGX checkout') {
			steps {
				sh "cd $WORKSPACE"
				sh "git clone https://github.com/NCATS-tangerine/kgx.git kgx"
				sh "ls -la"
				sh "ls -la kgx"
				sh "cd $WORKSPACE/kgx && pip3.7 install ."
				sh "mkdir $WORKSPACE/data"
				sh "mkdir $WORKSPACE/results"
			}
		}
		stage('Data download') {
			steps {

			}
		}
		stage('Build the KG') {
			steps {

			}
		}
		stage('Last stage') {
			steps {

			}
		}
	}
	post {
		always {
			// archive contents in results folder, only if the build is successful
            archiveArtifacts artifacts: 'results/*', onlyIfSuccessful: true

            // delete all created directories
            deleteDir()

            // clean workspace
			cleanWs()
		}
	}
}