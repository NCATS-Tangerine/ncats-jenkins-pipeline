# red-kg-load-pubmed pipeline

Pipeline to convert XML files to a generic RDF representing its structure, then transform it to the wanted datamodel by executing SPARQL inserts. 

## Run Jenkins

This pipeline needs to point to the Jenkins docker container to share `--volumes-from`. Hence it is better if the docker container is named as `jenkins-translator`, otherwise you will need to edit the link to `--volumes-from` to the ID or name of the Docker container.

```shell
docker run -it --name jenkins-translator \
  -p 3000:8080  \
  -v /data/jenkins:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  deepakunni3/ncats-jenkins 
```

