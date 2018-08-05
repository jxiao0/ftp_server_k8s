FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get update
RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv git curl

WORKDIR /root

RUN echo "deb http://packages.cloud.google.com/apt gcsfuse-xenial main" | tee /etc/apt/sources.list.d/gcsfuse.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN apt-get update
RUN apt-get install -y gcsfuse

RUN openssl req -newkey rsa:4096 -new -nodes -x509 -days 3650 -keyout key.pem -out key.pem -subj "/C=US/ST=IL/L=CHICAGO"
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel pyftpdlib==1.5.4 PyOpenSSL==18.0.0


ARG user=USERNAME
ARG pswd=PASSWORD
ARG root_dir=/root/sharedir
ARG ftpport=5518
ARG port_range=50000-50100
ARG perm=elr
ARG nat_addr=127.0.0.1
ARG lstn_addr=0.0.0.0



ENV USER=${user}
ENV PSWD=${pswd}
ENV ROOT_DIR=${root_dir}
ENV FTPPORT=${ftpport}
ENV PORT_RANGE=${port_range}
ENV PERM=${perm}
ENV NAT_ADDR=${nat_addr}
ENV LSTN_ADDR=${lstn_addr}


COPY ftp_server.py /root/ftp_server.py
RUN mkdir sharedir
EXPOSE ${ftpport} ${port_range}

CMD python3.6 /root/ftp_server.py --port=$FTPPORT --user=$USER --pswd=$PSWD --root_dir=$ROOT_DIR \
        --port_range=$PORT_RANGE --perm=$PERM --nat_addr=$NAT_ADDR --lstn_addr=$LSTN_ADDR



# export GCSFUSE_REPO=xenial
# echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" | tee /etc/apt/sources.list.d/gcsfuse.list
# curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -