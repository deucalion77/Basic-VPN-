FROM ubuntu:latest

RUN apt update && apt install -y python3 python3-pip && apt clean

RUN apt install -y net-tools 

RUN apt install -y iputils-ping iproute2 && apt clean

RUN mkdir -p /dev/net && \
    mknod /dev/net/tun c 10 200 && \
    chmod 600 /dev/net/tun

#RUN python3 vpn/vpn.py

CMD ["python3", "vpn/vpn.py"]
