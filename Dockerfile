FROM ubuntu:latest
MAINTAINER Gar Mendiola
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-init_1.1.3_amd64
RUN chmod +x /usr/local/bin/dumb-init
RUN mkdir -p /etc/phone-tree
COPY conf/phone-tree.yaml /etc/phone-tree/phone-tree.yaml
COPY webapp /webapp
WORKDIR /webapp
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["gunicorn", "--workers=4", "-b 0.0.0.0:5000","wsgi:app"]
