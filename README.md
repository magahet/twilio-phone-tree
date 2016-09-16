Twilio Phone Tree
=================
[![Build Status](https://travis-ci.org/magahet/twilio-phone-tree.svg?branch=master)](https://travis-ci.org/magahet/twilio-phone-tree)


Webapp to process Twilio webhooks and respond with an IVR phone tree defined by a simple yaml config.


# Deployment

## Manual Build

    make build
    cp /conf/phone-tree-example.yaml /conf/phone-tree.yaml
    make prod

## Docker Hub

    docker pull magahet/twilio-phone-tree
    docker run -d -p 5000:5000 -v conf:/etc/phone-tree magahet/twilio-phone-tree

# Usage

Modify phone-tree.yaml as needed. Point Twilio voice webhook to the launched service.
