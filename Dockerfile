FROM ubuntu:latest

RUN apt update && apt install -y python3 python3-pip && apt clean

RUN apt install -y net-tools 

RUN apt install -y iputils-ping

CMD ["sleep", "infinity"]
