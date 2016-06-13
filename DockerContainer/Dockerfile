#MAVEN BUILD CONTAINER 
FROM maven:3.3.9-jdk-8
MAINTAINER me@salih.xyz
RUN apt-get install git
ADD docker.sh /
#CMD ["echo",NAME]
RUN chmod +x /docker.sh
#CMD ["git","--version"]
ENTRYPOINT /docker.sh
