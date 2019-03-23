pipeline {
  agent any

  parameters {
    string(name: 'InputFile', defaultValue: '/var/jenkins_home/pubmed/pubmed19n0001-sample-6k.xml.gz', description: 'Path of the .xml or .xml.gz input file to convert to RDF.')
    string(name: 'GraphUri', defaultValue: 'https://w3id.org/data2services/graph/xml2rdf/pubmed', description: 'URI of the Graph to load')
    string(name: 'TriplestoreUri', defaultValue: 'http://graphdb.dumontierlab.com', description: 'URI of the repository used to insert the transformed RDF.')
    string(name: 'TriplestoreRepository', defaultValue: 'test_vincent', description: 'URI of the repository used to validate the graph using PyShEx')
    string(name: 'TriplestoreUsername', defaultValue: 'import_user', description: 'Username for the triplestore')
    string(name: 'TriplestorePassword', defaultValue: 'changeme', description: 'Password for the triplestore')
  }

  stages {
    stage('Build and install') {
      steps {
        sh 'git clone --recursive https://github.com/MaastrichtU-IDS/data2services-pipeline'
        sh 'docker build --rm -f "$WORKSPACE/data2services-pipeline/xml2rdf/Dockerfile" -t xml2rdf:latest $WORKSPACE/data2services-pipeline/xml2rdf'
        //sh "docker build --rm -t xml2rdf ${env.WORKSPACE}/data2services-pipeline/xml2rdf"
        sh 'docker build --rm -t rdf-upload $WORKSPACE/data2services-pipeline/RdfUpload'
        sh 'docker build --rm -t data2services-download $WORKSPACE/data2services-pipeline/data2services-download'
        //sh 'docker build -t rdf4j-sparql-operations ./data2services/rdf4j-sparql-operations'
        //sh './data2services-pipeline/build.sh'
      }
    }

    stage('data2services-download') {
      steps {
        sh "docker run -t --rm --volumes-from jenkins-translator data2services-download --download-datasets pubmed-sample --working-path /var/jenkins_home/pubmed"
        // TODO: iterate on files downloaded here
      }
    }

    stage('Process XML files') {
      steps {
        get_files()
        process_file(files)
      }
    }

    /*stage('RdfUpload') {
      steps {
        sh "docker run -t --rm --volumes-from jenkins-translator rdf-upload -if '${params.InputFile}.nq.gz' -url '${params.TriplestoreUri}' -rep '${params.TriplestoreRepository}' -un '${params.TriplestoreUsername}' -pw '${params.TriplestorePassword}'"
      }
    }*/

  }
  post {
    always {
      //archiveArtifacts artifacts: 'results/*', onlyIfSuccessful: true // archive contents in results folder
      deleteDir()
      cleanWs()
    }
  }
}

@NonCPS
def get_files() {
  def files = findFiles(glob: '*.xml.gz')
}

@NonCPS // has to be NonCPS or the build breaks on the call to .each
def process_file(list) {
    list.each { file ->
        echo "Processing file: ${file}"
        sh "docker run -t --rm --volumes-from jenkins-translator xml2rdf --inputfile '${file}' --outputfile '${file}.nq.gz' --graphuri ${params.GraphUri}"
        sh "docker run -t --rm --volumes-from jenkins-translator rdf-upload -if '${file}.nq.gz' -url '${params.TriplestoreUri}' -rep '${params.TriplestoreRepository}' -un '${params.TriplestoreUsername}' -pw '${params.TriplestorePassword}'"
    }
}