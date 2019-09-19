
FROM python:3.7-alpine
RUN apk update
RUN apk add -U curl bash
#RUN apt-get update
#RUN apt -y install curl
#RUN curl -Lo kubectl https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
#RUN chmod +x kubectl

#RUN curl -L -o /usr/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v1.6.0/bin/linux/amd64/kubectl && \
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin/kubectl

RUN apk add --no-cache ansible && \
rm -rf /tmp/* && \
rm -rf /var/cache/apk/*
RUN pip install --upgrade pip
RUN pip3 install tqdm
RUN pip3 install requests

RUN mkdir /etc/ansible/ /ansible && \
    echo "[local]" >> /etc/ansible/hosts && \
    echo "127.0.0.1" >> /etc/ansible/hosts

COPY ./ ./
