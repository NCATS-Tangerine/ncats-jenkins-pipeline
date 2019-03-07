FROM jenkins/jenkins:latest
MAINTAINER  Deepak Unni "deepak.unni3@gmail.com"

USER root

RUN apt-get update && apt-get -y upgrade && apt-get dist-upgrade && apt-get -y install build-essential python-dev python-setuptools python-pip python-smbus && apt-get -y install libncursesw5-dev libgdbm-dev libc6-dev zlib1g-dev libsqlite3-dev tk-dev libssl-dev openssl libffi-dev

RUN apt-get -y install wget curl make git-core vim lsof htop apt-transport-https ca-certificates gnupg2 software-properties-common

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && apt update && apt -y install docker-ce

RUN wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz && tar -xvzf Python-3.7.2.tgz && cd Python-3.7.2 && ./configure && make && make install

CMD ["/usr/local/bin/jenkins.sh"]
