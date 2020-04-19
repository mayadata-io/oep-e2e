---
id: dmaas
title: DMaaS
sidebar_label: Test Strategy
---
------

## DMaaS

Data Management as a Service provides backup & restore options to stateful applications.

### TestStrategy
- Configure DMAAS to provide scheduled backups with mixed types
    - Schedule starts with a full backup
    - Schedule should provide next 23 backups as incremental backups
    - Schedule should run every hour
    - Schedule should perform the 2nd full backup in its 25th iteration
    - Schedule should be able to backup the stateful application running on cStor volume
    - DMAAS should upload these backups to AWS S3
    - DMAAS should retain the S3 backups for last 3 days
- On a separate cluster
    - DMAAS should be able to connect to S3
    - DMAAS should be able to discover the backups
    - DMAAS should restore the stateful application using the oldest day's backups
    - DMAAS should restore a new application using latest but one day's backups
    - DMAAS should restore a new application using latest backups

_NOTE: This setup involves two workload setups_


### Test Case IDs -- Based on Storage Engine

| TCID                            |  GCP  |  KONVOY | AWS |
| ------------------------------- |  ---- |  ------ | --- |
| TCID-DMAAS-CSTOR                |       |         |     |
| TCID-DMAAS-JIVA                 |       |         |     |
| TCID-DMAAS-LOCAL-PV             |       |         |     |
| TCID-DMAAS-LOCAL-HOSTPATH       |       |         |     |

### Test Case IDs -- Based on Applications

| TCID                            |  GCP  | KONVOY  | AWS |
| ------------------------------- |  ---- | ------- | ----|
| TCID-DMAAS-CASSANDRA            |       |         |     |
| TCID-DMAAS-KAFKA                |       |         |     |
| TCID-DMAAS-MYSQL                |       |         |     |
| TCID-DMAAS-WORDPRESS            |       |         |     |
| TCID-DMAAS-NGINX                |       |         |     |
| TCID-DMAAS-PERCONA              |       |         |     |


## GLOSSARY
- WORKLOAD SETUP: A k8s cluster that runs continuously