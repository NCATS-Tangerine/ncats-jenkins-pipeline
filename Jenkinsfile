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
				sh "wget --no-clobber http://purl.obolibrary.org/obo/mondo.owl -O data/mondo.owl || true"
				sh "wget --no-clobber https://raw.githubusercontent.com/obophenotype/human-phenotype-ontology/master/hp.owl -O data/hp.owl || true"
				sh "wget --no-clobber https://raw.githubusercontent.com/The-Sequence-Ontology/SO-Ontologies/master/so.owl -O data/so.owl || true"
				// Download datasets
				sh "wget --no-clobber https://archive.monarchinitiative.org/latest/ttl/hpoa.ttl -O data/hpoa.ttl || true"
				sh "wget --no-clobber https://data.monarchinitiative.org/ttl/hgnc.ttl -O data/hgnc.ttl || true"
			}
		}
		stage('Building the Red KG') {
			steps {
				sh "python3.7 $WORKSPACE/scripts/download_red_kg.py"
			}
		}
		stage('Build the Monarch KG') {
			steps {
				sh "python3.7 $WORKSPACE/scripts/kgx_run.py"
			}
		}
		stage('Validate KG') {
			steps {
				sh "kgx validate results/monarch.csv.tar -o test/monarch/"
				sh "kgx validate results/red.csv.tar -o test/red/"
			}
		}
		stage('Merging the KG') {
			steps {
				sh "kgx merge -i results/red.csv.tar -i results/monarch.csv.tar -o results/merged.csv"
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
