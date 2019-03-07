start:
	docker run -d --rm -it -p 3000:8080 -v /var/run/docker.sock:/var/run/docker.sock --name ncats-jenkins deepakunni3/ncats-jenkins

stop:
	docker stop ncats-jenkins

logs:
	docker logs ncats-jenkins
