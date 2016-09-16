Twilio Phone Tree
=================

Webapp to process Twilio webhooks and respond with an IVR phone tree defined by a simple yaml config.


# Deployment

    make build
    cp /conf/phone-tree-example.yaml /conf/phone-tree.yaml
    make prod


# Usage

Modify phone-tree.yaml as needed. Point Twilio voice webhook to the launched service.
