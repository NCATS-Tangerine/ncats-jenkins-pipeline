pipeline {
	agent any

	environment {
		KGX_GIT='https://github.com/NCATS-tangerine/kgx.git'
		PYTHONPATH='$WORKSPACE/kgx'
		NEO4J_PASS = credentials('steveneo4j_pass')
	}
	options {
		// using the timestamps plugin we can add timestamps to the console log
		timestamps()
	}

	stages {
		stage('KGX checkout') {
			steps {
				sh "cd $WORKSPACE"
				sh "pip3.7 install git+https://github.com/NCATS-Tangerine/kgx@validate"
			}
		}
		stage('Data download') {
			steps {
				sh "ls db.csv.tar || kgx neo4j-download -a http://tkg-1.ncats.io -o db.csv"
			}
		}
		stage('Validate') {
			steps {
				sh "kgx validate db.csv.tar -o test_results"
			}
		}
	}

	post {
		always {
			// archive contents in results folder, only if the build is successful
			archiveArtifacts artifacts: 'test_results', onlyIfSuccessful: true

			// delete all created directories
			//deleteDir()

			// clean workspace
			//cleanWs()
		}
	}
}
