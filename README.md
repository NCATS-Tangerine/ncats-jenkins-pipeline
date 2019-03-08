# red-kg-validation pipeline

First version of a pipeline to validate the ncats-red-kg and compute [HCLS](https://www.w3.org/TR/hcls-dataset/#s6_6) statistics.

It takes a SPARQL endpoint to: 

* Perform [ShEx validation](https://github.com/hsolbrig/PyShEx) (on a subset of classes, here bl:Gene at the moment)
* Execute [SPARQL insert queries](https://github.com/vemonet/data2services-insert/tree/master/compute-statistics) to compute HCLS statistics for each graphs, and add those statistics to the dataset HCLS description

### Run Jenkins

This pipeline needs to point to the Jenkins docker container to share `--volumes-from`. Hence it is better if the docker container is named as `jenkins-translator`, otherwise you will need to edit the link to `--volumes-from` to the ID or name of the Docker container.

```shell
docker run -it --name jenkins-translator \
  -p 3000:8080  \
  -v /data/jenkins:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  deepakunni3/ncats-jenkins 
```

### Improvements

* Use Dockerized version of ShEx validation
* Make it more generic, to be able to compute statistics from any Translator data source (Reasoner API, Beacon API, KGX, Neo4j...)
* Avoid the need to use 2 different URLs for rdf4j triplestores (where we need to add `/statements` to udate). PyShEx should be able to log given username and password