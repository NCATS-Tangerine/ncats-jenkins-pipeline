# ncats-kg-release-pipeline

This is the repository for driving a Jenkins Multibranch pipeline.

Each branch will have its own version of `Jenkinsfile` that drives the pipeline.

Available branches:
* `master` - contains a [Jenkinsfile](https://github.com/deepakunni3/ncats-kg-release-pipeline/blob/master/Jenkinsfile) which serves as a template for a Jenkins build. The `master` branch should never generate any artifacts.
* `test` - contains a [Jenkinsfile](https://github.com/deepakunni3/ncats-kg-release-pipeline/blob/test/Jenkinsfile) which downloads test datasets, parses them using KGX to build a KG. The output is a KG as a csv.


### How do I run Jenkins

You can set up Jenkins locally, as a docker container or run on a server.

To run Jenkins as a docker container,
```
docker run -it -p 3000:8080 deepakunni3/ncats-jenkins
```

`deepakunni3/ncats-jenkins` is a Docker image that prepares an environment equipped to run KGX, and other tools, alongside Jenkins. This image is generated by this [Dockerfile](https://github.com/deepakunni3/ncats-kg-release-pipeline/blob/master/Dockerfile).
