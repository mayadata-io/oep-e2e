FROM python:3.7-alpine
RUN apk update
RUN apk add -U curl bash
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin/kubectl
RUN apk add --no-cache ansible && \
rm -rf /tmp/* && \
rm -rf /var/cache/apk/*
RUN pip install --upgrade pip
RUN mkdir /etc/ansible/ /ansible && \
    echo "[local]" >> /etc/ansible/hosts && \
    echo "127.0.0.1" >> /etc/ansible/hosts
COPY ./ ./
RUN pip3 install -r api_testing/requirements.txt
RUN cd api_testing && python setup.py install
RUN pip install pygithub

