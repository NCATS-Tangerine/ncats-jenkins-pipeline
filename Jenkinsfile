pipeline {
	agent any

	environment {
		KGX_GIT='https://github.com/NCATS-tangerine/kgx.git'
		PYTHONPATH='$WORKSPACE/kgx'
		NEO4J_PASS = credentials('neo4j_pass')
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
				sh "ls semmeddb.csv.tar || kgx neo4j-download -a http://34.229.55.225:7474 -u neo4j -p ${env.NEO4J_PASS} -o semmeddb.csv"
			}
		}
		stage('Validation') {
			steps {
				sh "kgx validate semmeddb.csv.tar -o test_results"
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
