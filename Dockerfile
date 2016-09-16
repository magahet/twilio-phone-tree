FROM ubuntu:latest
MAINTAINER Gar Mendiola
RUN apt-get update -y && \
    apt-get install -y \
        python-pip \
        python-dev \
        build-essential \
        wget
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-init_1.1.3_amd64
RUN chmod +x /usr/local/bin/dumb-init
RUN mkdir -p /etc/phone-tree
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY conf/phone-tree-example.yaml /etc/phone-tree/phone-tree.yaml
COPY webapp /webapp
WORKDIR /webapp
EXPOSE 5000
CMD ["/usr/bin/dumb-init", "--", "gunicorn", "--workers=4", "-b 0.0.0.0:5000","wsgi:app"]
