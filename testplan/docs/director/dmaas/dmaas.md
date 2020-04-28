---
id: dmaas
title: DMaaS
sidebar_label: Test Strategy
---
------

## DMaaS

Data Management as a Service provides backup & restore options to stateful applications.

### DMAAS -- TCID-DIR-DMAAS-MYSQL
As a DevOps admin, I manage MYSQL statefulset applications. These applications have a dependency on configmap. Both application as well as configmap reside in their specific namespace. I would like to have continuity plans for these applications. I want to take backup on a periodic basis & restore them optionally to verify if these backups are valid. I would like to maintain the count of backups so that these backups donot fill up the storage. I would like to store these backups at my desired S3 location.

| TCID                                             |  GCP  |  KONVOY | AWS |
| ------------------------------------------------ |  ---- |  ------ | --- |
| [TCID-DIR-DMAAS-MYSQL](TCID-DIR-DMAAS-MYSQL)     |       |         |     |


### DMASS -- TCID-DIR-DMAAS-CORTEX
As a DevOps admin, I manage cortex application. Cortex has a dependency on cassandra. I would like to have continuity plans for this application. I want to take on demand backup(s) of cortex & cassandra including their configuration & volumes. I want to restore the backup to verify before uploading the same to S3. I would like to be notified if my S3 location has enough space to accomodate new backups.

| TCID                                             |  GCP  |  KONVOY | AWS |
| ------------------------------------------------ |  ---- |  ------ | --- |
| [TCID-DIR-DMAAS-CORTEX](TCID-DIR-DMAAS-CORTEX)   |       |         |     |


### DMASS -- TCID-DIR-DMAAS-PORTAL
As a DevOps admin, I manage a portal which in turn is a suite of applications that includes multiple kubernetes deployments, statefulsets, configurations, serviceaccounts, secrets, custom resources & volumes. I would like to take periodic backups of this portal except a few resources namely nginx-controller deployment & ingress resources. I want these backups to be uploaded to multiple S3 locations. As part of the business continuity plan, I want to verify particular backups on an on-demand basis by restoring this portal on a different cluster & verifying its state.

| TCID                                             |  GCP  |  KONVOY | AWS |
| ------------------------------------------------ |  ---- |  ------ | --- |
| [TCID-DIR-DMAAS-PORTAL](TCID-DIR-DMAAS-PORTAL)   |       |         |     |


### DMASS -- TCID-DIR-DMAAS-PSP
As a DevOps admin, I manage multiple kubernetes applications. I have an extensive set of PodSecurityPolicies that govern the infrastructure policies in the cluster. I would like to take periodic backups these pod security policies and upload them to S3. As part of the my need to let all kubernetes clusters follow the same governance rules, I want to restore these pod security policies across other clusters.

| TCID                                             |  GCP  |  KONVOY | AWS |
| ------------------------------------------------ |  ---- |  ------ | --- |
| [TCID-DIR-DMAAS-PSP](TCID-DIR-DMAAS-PSP)         |       |         |     |

### DMASS -- TCID-DIR-DMAAS-EXCLUDE-SECRET
As a DevOps admin, I manage multiple kubernetes clusters. Each of these clusters cater to different lines of businesses. Any particular team's role vary depending on the cluster. As part of business continuity plans that adhere to above security need, I want to exclude backing up secrets. In other words, **no** secrets should get uploaded to S3.

| TCID                                                            |  GCP  |  KONVOY | AWS |
| --------------------------------------------------------------- |  ---- |  ------ | --- |
| [TCID-DIR-DMAAS-EXCLUDE-SECRET](TCID-DIR-DMAAS-EXCLUDE-SECRET)  |       |         |     |


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

| TCID                                                          |  GCP  | KONVOY  | AWS |
| ------------------------------------------------------------- |  ---- | ------- | ----|
| [TCID-DIR-DMAAS-SCHD-MONITOR](TCID-DIR-DMAAS-SCHD-MONITOR)    |       |         |     |

### Glossary

| Abbreviation     | Details                                           |
| ---------------- | ------------------------------------------------- |
| WORKLOAD         | A k8s cluster that runs continuously              |
| DIR              | Director                                          |
| SCHD             | Schedule                                          |
| LOCAL DEV        | Local Device operator                             |
| LOCAL HP         | Local HostPath operator                           |
