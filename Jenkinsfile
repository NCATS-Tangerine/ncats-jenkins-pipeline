pipeline {
  agent any

  parameters {
    string(name: 'GraphUri', defaultValue: 'https://w3id.org/data2services/graph/xml2rdf/pubmed', description: 'URI of the Graph to load')
    string(name: 'FinalSparqlRepositoryUri', defaultValue: 'http://graphdb.dumontierlab.com/repositories/public/statements', description: 'URI of the repository used to insert the transformed RDF.')
    string(name: 'BufferSparqlRepositoryUri', defaultValue: 'http://graphdb.dumontierlab.com/repositories/public/statements', description: 'URI of the repository used to validate the graph using PyShEx')
    string(name: 'TriplestoreUsername', defaultValue: 'import_user', description: 'Username for the triplestore')
    string(name: 'TriplestorePassword', defaultValue: 'changeme', description: 'Password for the triplestore')
  }

  stages {
    stage('Build and install') {
      steps {
        sh 'git clone --recursive https://github.com/MaastrichtU-IDS/data2services-pipeline'
        sh 'docker build --rm -f "$WORKSPACE/data2services-insert/xml2rdf/Dockerfile" -t xml2rdf:latest $WORKSPACE/data2services-insert/xml2rdf'
        //sh "docker build --rm -t xml2rdf ${env.WORKSPACE}/data2services-pipeline/xml2rdf"
        //sh 'docker build -t rdf-upload ./data2services/RdfUpload'
        //sh 'docker build -t rdf4j-sparql-operations ./data2services/rdf4j-sparql-operations'
        //sh './data2services-pipeline/build.sh'
      }
    }

    stage('xml2rdf') {
      steps {
        sh "docker run -t --rm --volumes-from jenkins-translator xml2rdf -f '/data/pubmed/pubmed18n0001.xml.gz' -ep '${params.FinalSparqlRepositoryUri}' -un ${params.TriplestoreUsername} -pw ${params.TriplestorePassword}"
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