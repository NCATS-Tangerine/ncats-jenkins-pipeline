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
		stage('KGX installation') {
			steps {
				sh "cd $WORKSPACE"
				sh "pip3.7 install --no-cache-dir --upgrade git+https://github.com/NCATS-tangerine/kgx.git@monarch-build-workflow"
				sh "mkdir -p $WORKSPACE/data"
				sh "mkdir -p $WORKSPACE/results"
			}
		}
		stage('Data download') {
			steps {
				sh "ls -la data/"
				// Download ontology files
				sh "make download"
			}
		}
		stage('Building the Monarch KG') {
			steps {
				sh "python3.7 $WORKSPACE/scripts/monarch_build.py"
			}
		}
		stage('Validate KG') {
			steps {
				sh "kgx validate results/monarch.csv.tar -o test/monarch/"
			}
		}
		stage('Last stage') {
			steps {
				sh "ls -la results/"
			}
		}
	}
	post {
		always {
			// archive contents in results folder, only if the build is successful
			archiveArtifacts artifacts: '*', onlyIfSuccessful: true

			// delete all created directories
			//deleteDir()

			// clean workspace
			//cleanWs()
		}
	}
}
