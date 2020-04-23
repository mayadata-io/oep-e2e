---
id: dmaas
title: DMaaS
sidebar_label: Test Strategy
---
------

## DMaaS

Data Management as a Service provides backup & restore options to stateful applications.

### DMAAS Scheduling -- TCID-DIR-DMAAS-SCHD
As a DevOps admin, I want Director to provide a backup & restore option for my teams to self manage their k8s application continuity plans. I would expect my teams to have the ability to configure backup & restore similar to the following steps:

- Configure Director to provide scheduled backups with mixed types
    - Schedule starts with a full backup
    - Schedule should provide next 23 backups as incremental backups
    - Schedule should run every hour
    - Schedule should perform the 2nd full backup in its 25th iteration
    - Schedule should be able to backup the stateful application running on openebs volume
    - Director should upload these backups to AWS S3
    - Director should retain the S3 backups for last 3 days
- On a separate cluster
    - Director should be able to connect to S3
    - Director should be able to discover the backups
    - Director should restore the stateful application using the oldest day's backups
    - Director should restore a new application using latest but one day's backups
    - Director should restore a new application using latest backups

_NOTE: This setup involves two workload setups_

#### Test Case IDs -- Based on Storage Engine

| TCID                                                              |  GCP  |  KONVOY | AWS |
| ----------------------------------------------------------------- |  ---- |  ------ | --- |
| [TCID-DIR-DMAAS-SCHD-CSTOR](TCID-DIR-DMAAS-SCHD-CSTOR)            |       |         |     |
| [TCID-DIR-DMAAS-SCHD-JIVA](TCID-DIR-DMAAS-SCHD-JIVA)              |       |         |     |
| [TCID-DIR-DMAAS-SCHD-LOCAL-DEV](TCID-DIR-DMAAS-SCHD-LOCAL-DEV)    |       |         |     |
| [TCID-DIR-DMAAS-SCHD-LOCAL-HP](TCID-DIR-DMAAS-SCHD-LOCAL-HP)      |       |         |     |

#### Test Case IDs -- Based on Applications

| TCID                                                              |  GCP  | KONVOY  | AWS |
| ----------------------------------------------------------------- |  ---- | ------- | ----|
| [TCID-DIR-DMAAS-SCHD-CASSANDRA](TCID-DIR-DMAAS-SCHD-CASSANDRA)    |       |         |     |
| [TCID-DIR-DMAAS-SCHD-KAFKA](TCID-DIR-DMAAS-SCHD-KAFKA)            |       |         |     |
| [TCID-DIR-DMAAS-SCHD-MYSQL](TCID-DIR-DMAAS-SCHD-MYSQL)            |       |         |     |
| [TCID-DIR-DMAAS-SCHD-WORDPRESS](TCID-DIR-DMAAS-SCHD-WORDPRESS)    |       |         |     |
| [TCID-DIR-DMAAS-SCHD-NGINX](TCID-DIR-DMAAS-SCHD-NGINX)            |       |         |     |
| [TCID-DIR-DMAAS-SCHD-PERCONA](TCID-DIR-DMAAS-SCHD-PERCONA)        |       |         |     |


### DMAAS Monitor -- TCID-DIR-DMAAS-SCHD-MONITOR
This strategy is a continuation of above TCID-DMAAS-SCHD test strategy. As a DevOps admin, I would like to monitor the following:
- view the application continuity plans of my teams
- view the S3 usage on a per team basis
- view connectivity to backup as well as restore cluster


### Glossary

| Abbreviation     | Details                                           |
| ---------------- | ------------------------------------------------- |
| WORKLOAD         | A k8s cluster that runs continuously              |
| DIR              | Director                                          |
| SCHD             | Schedule                                          |
| LOCAL DEV        | Local Device operator                             |
| LOCAL HP         | Local HostPath operator                           |
