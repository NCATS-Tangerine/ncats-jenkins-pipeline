pipeline {
  agent any

  parameters {
    string(name: 'InputFile', defaultValue: '/var/jenkins_home/pubmed/pubmed18n0001.xml.gz', description: 'Path of the .xml or .xml.gz input file to convert to RDF.')
    string(name: 'GraphUri', defaultValue: 'https://w3id.org/data2services/graph/xml2rdf/pubmed', description: 'URI of the Graph to load')
    string(name: 'TriplestoreUri', defaultValue: 'http://graphdb.dumontierlab.com', description: 'URI of the repository used to insert the transformed RDF.')
    string(name: 'TriplestoreRepository', defaultValue: 'vincent_test', description: 'URI of the repository used to validate the graph using PyShEx')
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
        //sh 'docker build -t rdf4j-sparql-operations ./data2services/rdf4j-sparql-operations'
        //sh './data2services-pipeline/build.sh'
      }
    }

    stage('xml2rdf') {
      steps {
        sh "docker run -t --rm --volumes-from jenkins-translator xml2rdf --inputfile '${params.InputFile}' --outputfile '${params.InputFile}.nq.gz' --graphuri ${params.GraphUri}"
      }
    }

    stage('RdfUpload') {
      steps {
        sh "docker run -it --rm -v /data/rdfu:/data rdf-upload -if '${params.InputFile}.nq.gz' -url '${params.TriplestoreUri}' -rep '${params.TriplestoreRepository}' -un '${params.TriplestoreUsername}' -pw '${params.TriplestorePassword}'"
      }
    }

    /*stage('RDFUnit') {
      steps {
        sh 'docker run --rm -t --volumes-from jenkins-translator -v /data/translator:/data dqa-rdfunit  -o ttl -d "http://graphdb.dumontierlab.com/repositories/ncats-red-kg" \
        -e "http://graphdb.dumontierlab.com/repositories/ncats-red-kg" -f "$WORKSPACE/rdfunit" -s "https://raw.githubusercontent.com/biolink/biolink-model/master/ontology/biolink.ttl" -g "https://w3id.org/data2services/graph/biolink/date"'
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