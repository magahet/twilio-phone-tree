Twilio Phone Tree
=================

Webapp to process Twilio webhooks and respond with an IVR phone tree defined by a simple yaml config.


# Deployment

1. Copy /conf/phone-tree-example.yaml to /conf/phone-tree.yaml
2. make build (does a Docker build)
3. make run


# Usage

Modify phone-tree.yaml as needed. Point Twilio voice webhook to the launched service.
